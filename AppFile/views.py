from flask import render_template, request
from werkzeug.utils import secure_filename
from AppFile import app, defs
import os

@app.route("/")
def index1():
    return render_template("./HTMLFile/home.html")

@app.route("/2")
def index2():
    return render_template("./HTMLFile/upload.html", STR=defs.func())

@app.route("/3", methods=['POST', 'GET'])
def setting():
    if request.method == 'GET':
        return "Please upload video file"
    
    elif request.method == 'POST':
        video = request.files['video']
        
        if video.name == '':
            return "There is no file name."
        
        if video:
            filename = secure_filename(video.filename)
        
        video.save("./"+filename)
        return os.getcwd()