from flask import Flask
from flask import render_template
from datetime import datetime
from . import app

@app.route("/_status")
def status():
    return "ok"

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

