from flask import redirect, render_template, request, send_from_directory
from app import app
from repositories import books_repository
from services import source_service
from services import bibtex_service
import os

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add(service = source_service):
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
    books = source_service.get_books(books_repository)
    return render_template("list.html", sources=books)

@app.route("/reset", methods=["GET"])
def empty_sources():
    source_service.delete_all_books(books_repository)
    return redirect("/")

@app.route("/bibtex", methods=["GET"])
def create_bibtex_file(bibtex_service = bibtex_service):
    bibtex_service.create_bibtex_file("references", source_service)
    return render_template("bibtex.html")

@app.route("/download", methods=["GET"])
def download_bibtex_file():
    upload = os.path.join(app.root_path, "bibtex_files")
    return send_from_directory(upload, "references.bib")
