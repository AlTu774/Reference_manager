from flask import redirect, render_template, request
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    
    if request.method == "POST":
        return render_template("add.html")

@app.route("/list", methods=["GET"])
def list_sources():
    return render_template("list.html")
