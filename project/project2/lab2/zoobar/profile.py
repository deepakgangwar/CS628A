from flask import g
from debug import *

import rpclib
import traceback

def run_profile(user):
    try:
        pcode = user.profile.encode('ascii', 'ignore')
        pcode = pcode.replace('\r\n', '\n')
        log(user)
        log(g.user)
        log(g.user.person)
        with rpclib.client_connect('/profilesvc/sock') as c:
            return c.call('run', pcode=pcode,
                                 user=user.username,
                                 visitor=g.user.person.username)
    except Exception, e:
        traceback.print_exc()
        return 'Exception: ' + str(e)
