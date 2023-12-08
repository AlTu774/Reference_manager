from sqlalchemy import text
from db import db

def insert_book(book, user_id):
    sql = """INSERT INTO books (tag, title, author, publish_year, publisher)
        VALUES (:tag, :title, :author, :publish_year, :publisher)"""
    db.session.execute(text(sql), {"tag":book.tag,
                                    "title":book.title,
                                    "author":book.author,
                                   "publish_year":book.publish_year,
                                     "publisher":book.publisher,
                                     "user_id":user_id})
    db.session.commit()

def get_books():
    sql = "SELECT id, tag, title, author, publish_year, publisher FROM books"
    return db.session.execute(text(sql)).fetchall()

def get_my_books(user_id):
    sql = "SELECT id, tag, title, author, publish_year, publisher FROM books WHERE user_id=:user_id"
    return db.session.execute(text(sql), {"user_id":user_id}).fetchall()

def delete_all_books():
    sql = "DELETE FROM books"
    db.session.execute(text(sql))
    db.session.commit()

def delete_my_books(user_id):
    sql = "DELETE FROM book WHERE user_id=:user_id"
    db.session.execute(text(sql), {"user_id":user_id})