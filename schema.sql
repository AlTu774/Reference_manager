DROP TABLE IF EXISTS Books CASCADE;
DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    tag TEXT,
    title TEXT,
    author TEXT,
    publish_year INT,
    publisher TEXT
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);