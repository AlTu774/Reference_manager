from sqlalchemy import text
from db import db

def insert_tag(user_id, tag_name):
    sql = """INSERT INTO tags (creator_id, tag_name)
        VALUES (:user_id, :tag_name)"""
    db.session.execute(sql, {"user_id": user_id, "tag_name": tag_name})
    db.session.commit()
    return True

def tag_book(tag_id, book_id):
    sql = """INSERT INTO tagged_books (tag_id, book_id)
        VALUES (:tag_id, :book_id)"""
    db.session.execute(sql, {"tag_id": tag_id, "book_id": book_id})
    db.session.commit()
    return True

def get_tags_by_user_id(user_id):
    sql = """SELECT id, tag_name FROM tags WHERE user_id=:user_id"""
    taglist = db.session.execute(sql, {"user_id": user_id}).fetchall()

    return taglist

def get_tags_by_book_id(book_id):
    sql = """SELECT id AS tagging_id, tags.id, tag_name
        FROM tagged_books INNER JOIN tags ON tagged_books.tag_id=tags.id
        WHERE tagged_books.book_id=:book_id"""

    tags_of_book = db.session.execute(sql, {"book_id": book_id}).fetchall()

    return tags_of_book
