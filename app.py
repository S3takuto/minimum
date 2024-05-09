from flask import Flask
from AppFile import app
#app = Flask(__name__)

@app.route("/")
def index1():
    return "index1"

@app.route("/2")
def index2():
    return "index2"

if __name__ == "__main__":
    app.run(debug=True)