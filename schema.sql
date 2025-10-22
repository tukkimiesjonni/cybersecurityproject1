CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    password TEXT
);

CREATE TABLE threads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    content TEXT,
    published TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    thread_id INTEGER,
    comment TEXT,
    published TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (thread_id) REFERENCES threads(id)
);

CREATE TABLE votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    thread_id INTEGER,
    vote INTEGER,
    FOREIGN KEY (thread_id) REFERENCES threads(id)
);
