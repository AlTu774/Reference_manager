DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    latex_key TEXT,
    title TEXT,
    author TEXT,
    publish_year INT,
    user_id INT REFERENCES users,
    publisher TEXT
);
