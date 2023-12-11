DROP TABLE IF EXISTS Books CASCADE;
DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    tag VARCHAR,
    title VARCHAR(70),
    author VARCHAR(70),
    publish_year INT(4),
    publisher VARCHAR
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    password VARCHAR
);