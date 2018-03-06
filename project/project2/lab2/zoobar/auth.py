from zoodb import *
from debug import *

import hashlib
import random
import os
import pbkdf2
import bank_client

def newtoken(db, person):
    hashinput = "%s%.10f" % (person.password, random.random())
    person.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return person.token

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == unicode(pbkdf2.PBKDF2(password, cred.salt).hexread(32)):
        return newtoken(db, cred)
    else:
        return None

def register(username, password):
    db = person_setup()
    db1 = cred_setup()
    person = db.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newcred = Cred()
    salt = os.urandom(5).decode("latin-1")
    password = unicode(pbkdf2.PBKDF2(password, salt).hexread(32))
    newperson.username = username
    newcred.password = password
    newcred.username = username
    newcred.salt = salt
    db.add(newperson)
    db1.add(newcred)
    db.commit()
    db1.commit()
    bank_client.register(username)
    return newtoken(db1, newcred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False
