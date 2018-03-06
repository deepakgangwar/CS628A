#!/usr/bin/python

import rpclib
import sys
import os
import sandboxlib
import urllib
import hashlib
import socket
import bank_client
import auth_client
import zoodb
import md5

from debug import *

## Cache packages that the sandboxed code might want to import
import time
import errno

class ProfileAPIServer(rpclib.RpcServer):
    def __init__(self, user, visitor):
        self.user = user
        self.visitor = visitor
        db = zoodb.cred_setup()
        cred = db.query(zoodb.Cred).get(user)
        self.token = cred.token
        os.setgid(61011)
        os.setuid(61018)

    def rpc_get_self(self):
        return self.user

    def rpc_get_visitor(self):
        return self.visitor

    def rpc_get_xfers(self, username):
        xfers = []
        for xfer in bank_client.get_log(username):
            log(xfer)
            xfers.append({ 'sender': xfer['sender'],
                           'recipient': xfer['recipient'],
                           'amount': xfer['amount'],
                           'time': xfer['time'],
                         })
        return xfers

    def rpc_get_user_info(self, username):
        person_db = zoodb.person_setup()
        p = person_db.query(zoodb.Person).get(username)
        if not p:
            return None
        return { 'username': p.username,
                 'profile': p.profile,
                 'zoobars': bank_client.balance(username),
               }

    def rpc_xfer(self, target, zoobars):
        bank_client.transfer(self.user, target, zoobars, self.token)

def run_profile(pcode, profile_api_client):
    globals = {'api': profile_api_client}
    exec pcode in globals

class ProfileServer(rpclib.RpcServer):
    def rpc_run(self, pcode, user, visitor):
        #uncomment the 2 commented lines and also line no.63 in chroot-setup to enable additional security such that if a profile breaks jail then also it's not able to access other's files
        q = 12356
        #q = int(''.join(str(ord(c)) for c in user)) % 2147360190 + 12355
        uid = q
        m = md5.new(user).hexdigest()

        userdir = '/tmp'+'/' + m
        #userdir = '/tmp'+'/' + str(q)
        if not os.path.isdir(userdir):
            os.mkdir(userdir, 0770)
            os.chown(userdir,q,q)

        (sa, sb) = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM, 0)
        pid = os.fork()
        if pid == 0:
            if os.fork() <= 0:
                sa.close()
                ProfileAPIServer(user, visitor).run_sock(sb)
                sys.exit(0)
            else:
                sys.exit(0)
        sb.close()
        os.waitpid(pid, 0)

        sandbox = sandboxlib.Sandbox(userdir, uid, '/profilesvc/lockfile')
        with rpclib.RpcClient(sa) as profile_api_client:
            return sandbox.run(lambda: run_profile(pcode, profile_api_client))

(_, dummy_zookld_fd, sockpath) = sys.argv

s = ProfileServer()
s.run_sockpath_fork(sockpath)
