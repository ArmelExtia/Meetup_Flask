from flask import render_template,request,redirect,current_app

from ..routes import api

@api.route("/")
def test():
    return "hello"
