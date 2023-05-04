from flask import Flask, render_template, request
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.args.get("username", "World")
    return render_template("welcome.html", name=username)