from os import getenv, environ
from flask_sqlalchemy import SQLAlchemy
from src.app import app

DATABASE_URL = environ.get("DATABASE_URL")
DATABASE_URL = DATABASE_URL.replace('://', 'ql://', 1) \
    if DATABASE_URL.startswith('postgres://') else DATABASE_URL
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL


# Checks if database is active, and pings it before submitting requests
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}

db = SQLAlchemy(app)
