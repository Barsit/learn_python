from flask import Flask

app = Flask(__name__)

@app.route("/hi")
def hello():
    return "Hello, World!"