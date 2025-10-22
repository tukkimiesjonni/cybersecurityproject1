import sqlite3
from contextlib import closing

DATABASE = "database.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def execute_query(query, params=(), fetch=False):
    with closing(get_connection()) as conn:
        with conn:
            cursor = conn.execute(query, params)
            conn.commit()
            if fetch:
                return cursor.fetchall()
