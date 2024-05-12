from flask import render_template
from AppFile import app, defs

@app.route("/")
def index1():
    return render_template("./HTMLFile/home.html")

@app.route("/2")
def index2():
    return render_template("./HTMLFile/upload.html", STR=defs.func())

@app.route("/3")
def setting(method=['POST', 'GET']):
    return "index3"