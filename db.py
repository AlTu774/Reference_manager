from os import environ
from flask_sqlalchemy import SQLAlchemy
from app import app

MODE = environ.get("MODE") or "production"

DATABASE_URL = environ.get("DATABASE_URL")
if MODE == "test":
    DATABASE_URL = environ.get("TEST_DATABASE_URL")
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace('://', 'ql://', 1) \
        if DATABASE_URL.startswith('postgres://') else DATABASE_URL
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL



db = SQLAlchemy(app)
