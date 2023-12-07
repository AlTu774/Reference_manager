const { Client } = require('pg');

const pgclient = new Client({
    host: process.env.POSTGRES_HOST,
    port: process.env.POSTGRES_PORT,
    user: 'postgres',
    password: 'postgres',
    database: 'postgres'
});

pgclient.connect();

const table = 'CREATE TABLE Books (id SERIAL PRIMARY KEY, tag TEXT, title TEXT, author TEXT, publish_year INT, publisher TEXT)'
const text = 'CREATE TABLE Users (id SERIAL PRIMARY KEY, username TEXT, password TEXT)'

pgclient.query(table, (err, res) => {
    if (err) throw err
});

pgclient.query(text, (err, res) => {
    if (err) throw err
});
