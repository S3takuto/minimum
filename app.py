from flask import Flask

app = Flask(__name__)
@app.route("/")
def index1():
    return "index1"

@app.route("/2")
def index2():
    import defs
    str = defs.func1()
    return str

if __name__ == "__main__":
    app.run()