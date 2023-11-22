from flask import redirect, render_template, request
from app import app
from repositories import books_repository

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    
    if request.method == "POST":
        tag = request.form["tag"]
        title = request.form["title"]
        author = request.form["author"]
        publish_year = request.form["publish_year"]
        publisher = request.form["publisher"]
        books_repository.insert_book(tag, title, author, publish_year, publisher)

        return render_template("add.html")

@app.route("/list", methods=["GET"])
def list_sources():
    return render_template("list.html")
