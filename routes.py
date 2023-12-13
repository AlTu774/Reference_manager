import os
from flask import (
    redirect, render_template, request, send_from_directory, session)
from app import app
from repositories import books_repository
from repositories import users_repository
from repositories import tags_repository
from services import source_service
from services import bibtex_service



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add(service = source_service):
    if request.method == "GET":
        tag_list = tags_repository.get_tags_by_user_id(session["user_id"])
        return render_template("add.html", tag_list=tag_list)

    if request.method == "POST":
        latex_key = request.form["latex_key"]
        title = request.form["title"]
        author = request.form["author"]
        publish_year = request.form["publish_year"]
        publisher = request.form["publisher"]
        service.insert_book(latex_key, title, author,
                                   publish_year, publisher, books_repository,
                                   session["user_id"])

    tag_list = tags_repository.get_tags_by_user_id(session["user_id"])

    return render_template("add.html", tag_list=tag_list)

@app.route("/tags", methods=["GET", "POST"])
def tags():
    error = None
    if request.method == "GET":
        return render_template("tags.html")

    if request.method == "POST":
        tag_name = request.form["tag_name"]
        user_id = request.form["user_id"]

        tag_tuples = tags_repository.get_tags_by_user_id(user_id)
        user_tags = [tag[1] for tag in tag_tuples]

        if tag_name not in user_tags:
            tags_repository.insert_tag(user_id, tag_name)
            return redirect("/")

    error = "Tag by this name already exists."
    return render_template("tags.html", error=error)


@app.route("/list", methods=["GET"])
def list_sources():
    books = source_service.get_books(books_repository, session["user_id"])
    return render_template("list.html", sources=books)

@app.route("/reset", methods=["GET"])
def empty_sources():
    source_service.delete_my_books(books_repository, session["user_id"])
    return redirect("/")

@app.route("/reset_users", methods=["GET"])
def reset_users():
    users_repository.delete_all_users()
    return redirect("/")


@app.route("/bibtex", methods=["GET"])
def create_bibtex_file(service = bibtex_service):
    service.create_bibtex_file("references", source_service, books_repository,
                               session["user_id"])
    return render_template("bibtex.html")

@app.route("/download", methods=["GET"])
def download_bibtex_file():
    upload = os.path.join(app.root_path, "bibtex_files")
    return send_from_directory(upload, "references.bib")

@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        login_check = users_repository.login(username, password)
        if not isinstance(login_check, str):
            session["username"] = username
            session["user_id"] = login_check
            return redirect("/")

    error = login_check
    return render_template("login.html", error=error)

@app.route("/register", methods=["POST", "GET"])
def register():
    error = None

    if request.method == "GET":
        return render_template("register.html", error=error)

    if request.method == "POST":
        all_usernames = users_repository.get_all_usernames()
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        if username in all_usernames:
            error = "Username has already been taken"
        elif password != password2:
            error = "Passwords do not match"
        else:
            users_repository.register(username, password)
            user_id = users_repository.login(username, password)
            session["username"] = username
            session["user_id"] = user_id
            return redirect("/")

    return render_template("register.html", error=error)

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]

    return redirect("/")
