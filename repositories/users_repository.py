from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db



def register(username, password):
    hash_value = generate_password_hash(password)
    sql = """INSERT INTO Users (username, password)
    VALUES (:username, :password)"""
    db.session.execute(text(sql), {"username":username, "password":hash_value})
    db.session.commit()

def login(username, password):
    sql = "SELECT id, password FROM Users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()

    if not user:
        return "Invalid username"

    hash_value = user.password

    if not check_password_hash(hash_value, password):
        return "Invalid password"
    return True

def get_all_usernames():
    sql = "SELECT username FROM Users"
    result = db.session.execute(text(sql))
    return [row[0] for row in result.fetchall()]

def delete_all_users():
    sql = "DELETE FROM Users"
    db.session.execute(text(sql))
    db.session.commit()
