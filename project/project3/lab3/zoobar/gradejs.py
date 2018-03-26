from flask import g, render_template, make_response

import login
from zoodb import *
from debug import catch_err

@catch_err
def gradejs():
    if login.logged_in():
        return render_template("grade.js")
    else:
        return ""
