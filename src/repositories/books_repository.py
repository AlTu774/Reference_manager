from sqlalchemy import text
from db import db

def insert_book(tag, title, author, publish_year, publisher):
    sql = """INSERT INTO books (tag, title, author, publish_year, publisher)
        VALUES (:tag, :title, :author, :publish_year, :publisher)"""
    db.session.execute(text(sql), {"tag":tag, "title":title, "author":author,
                                   "publish_year":publish_year, "publisher":publisher})
    db.session.commit()
