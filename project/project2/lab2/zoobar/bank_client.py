from debug import *
from zoodb import *
import rpclib

def balance(username):
    ## Fill in code here.
    socket = "/banksvc/sock"
    kwargs = {"username":username}
    with rpclib.client_connect(socket) as r:
        return r.call("balance",**kwargs)


def get_log(username):
    socket = "/banksvc/sock"
    kwargs = {"username":username}
    with rpclib.client_connect(socket) as r:
        return r.call("get_log",**kwargs)

def transfer(sender, recipient, zoobars, token):
    ## Fill in code here.
    socket = "/banksvc/sock"
    kwargs = {"sender" : sender, "recipient" : recipient, "zoobars" : zoobars, "token": token}
    with rpclib.client_connect(socket) as r:
        return r.call("transfer",**kwargs)

def register(username):
    socket = "/banksvc/sock"
    kwargs = {"username":username}
    with rpclib.client_connect(socket) as r:
        return r.call("register",**kwargs)
