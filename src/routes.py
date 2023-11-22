from flask import redirect, render_template, request
from src.app import app
from src.repositories import books_repository
from src.services import source_service

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
        source_service.insert_book(tag, title, author, publish_year, publisher, books_repository)

        return render_template("add.html")

@app.route("/list", methods=["GET"])
def list_sources():
    return render_template("list.html")
