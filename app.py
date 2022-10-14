from flask import Flask
app = Flask(__name__)

@app.route("/_status")
def status():
    return "ok"

@app.route("/")
def home():
    return "Hello, Flask!"