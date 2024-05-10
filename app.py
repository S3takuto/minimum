from flask import Flask

app = Flask(__name__)
@app.route("/")
def index1():
    return "index1"

@app.route("/2")
def index2():
    return "index2"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8181)