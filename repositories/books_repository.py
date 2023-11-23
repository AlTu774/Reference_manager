from sqlalchemy import text
from db import db

def insert_book(book):
    sql = """INSERT INTO books (tag, title, author, publish_year, publisher)
        VALUES (:tag, :title, :author, :publish_year, :publisher)"""
    db.session.execute(text(sql), {"tag":book.tag, "title":book.title, "author":book.author,
                                   "publish_year":book.publish_year, "publisher":book.publisher})
    db.session.commit()

def get_books():
    sql = "SELECT id, tag, title, author, publish_year, publisher FROM books"
    return db.session.execute(text(sql)).fetchall()
