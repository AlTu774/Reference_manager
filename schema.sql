DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS tags CASCADE;
DROP TABLE IF EXISTS tagged_books CASCADE;

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
    publish_year INTEGER,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    publisher TEXT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users ON DELETE CASCADE,
    tag_name TEXT
);

CREATE TABLE tagged_books (
    id SERIAL PRIMARY KEY,
    tag_id INTEGER REFERENCES tags ON DELETE CASCADE,
    book_id INTEGER REFERENCES books ON DELETE CASCADE
);
