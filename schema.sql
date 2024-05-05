CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    password TEXT
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    title TEXT,
    content TEXT,
    published TIMESTAMP
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    thread_id INTEGER REFERENCES threads,
    comment TEXT,
    published TIMESTAMP
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    thread_id INTEGER REFERENCES threads,
    vote INTEGER
);


/*

New schema with third normal form

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    password TEXT
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    title TEXT,
    published TIMESTAMP
);

CREATE TABLE thread_content (
    thread_id INTEGER PRIMARY KEY REFERENCES threads,
    content TEXT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    thread_id INTEGER REFERENCES threads,
    comment TEXT,
    published TIMESTAMP
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    thread_id INTEGER REFERENCES threads,
    vote INTEGER
);

*/
