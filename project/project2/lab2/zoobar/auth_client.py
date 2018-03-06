from debug import *
from zoodb import *
import rpclib

def login(username, password):
    ## Fill in code here.
    socket = "/authsvc/sock"
    kwargs = {"username":username,"password":password}
    with rpclib.client_connect(socket) as r:
        return r.call("login",**kwargs)


def register(username, password):
    socket = "/authsvc/sock"
    kwargs = {"username":username,"password":password}
    with rpclib.client_connect(socket) as r:
        return r.call("register",**kwargs)

def check_token(username, token):
    ## Fill in code here.
    socket = "/authsvc/sock"
    kwargs = {"username":username,"token":token}
    with rpclib.client_connect(socket) as r:
        return r.call("check_token",**kwargs)
