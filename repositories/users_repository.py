from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db



USERS_TABLE = "Users"
USERNAME_COL = "username"
PASSWORD_COL = "password"

def register(username, password):
    hash_value = generate_password_hash(password)
    sql = f"""INSERT INTO {USERS_TABLE} ({USERNAME_COL}, {PASSWORD_COL})
              VALUES (:username, :password)"""
    db.session.execute(text(sql), {"username": username, "password": hash_value})
    db.session.commit()

def login(username, password):
    sql = f"SELECT id, {PASSWORD_COL} FROM {USERS_TABLE} WHERE {USERNAME_COL}=:username"
    result = db.session.execute(text(sql), {"username": username})
    user = result.fetchone()

    if not user:
        return "Invalid username"

    hash_value = user[1]

    if not check_password_hash(hash_value, password):
        return "Invalid password"
    return user.id

def get_all_usernames():
    sql = f"SELECT {USERNAME_COL} FROM {USERS_TABLE}"
    result = db.session.execute(text(sql))
    return [row[0] for row in result.fetchall()]

def delete_all_users():
    sql = f"DELETE FROM {USERS_TABLE}"
    db.session.execute(text(sql))
    db.session.commit()
