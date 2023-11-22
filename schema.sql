DROP TABLE IF EXISTS Books CASCADE;

CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    tag TEXT,
    title TEXT,
    author TEXT,
    publish_year INT,
    publisher TEXT
);
