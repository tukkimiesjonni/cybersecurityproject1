import os
from hashlib import sha256
from db import db
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from datetime import datetime


def get_timestamp():
    time = datetime.now()
    return time


def create_thread(title, content):
    status = False

    print(title, content)

    time = get_timestamp()

    query = text("""
        INSERT INTO threads (title, content, published)
        VALUES (:title, :content, :published)
    """)

    db.session.execute(query, {"title":title, "content":content, "published":time})
    db.session.commit()
    print("thread added")
    return True


def get_thread_id(thread):
    query = text("""
        SELECT id FROM threads
        WHERE title = (:title)
    """)

    query_result = db.session.execute(query, {"title":thread})
    thread_id = query_result.fetchone()[0]

    return thread_id


def get_user_id(username):
    query = text("""
        SELECT id FROM users
        WHERE name = (:username)
    """)

    query_result = db.session.execute(query, {":username":username})
    user_id = query_result.fetchone()[0]

    return user_id


def add_comment(thread, comment):

    time = get_timestamp()
    thread_id = get_thread_id(thread)
    user_id = get_user_id(session["username"])


    query = text("""
        INSERT INTO comments (user_id, thread_id, comment, published)
        VALUES (:user_id, :thread_id, :comment, :time)
    """)

    db.session.execute(query, {"user_id":user_id, "thread_id":thread_id, "comment":comment, "time":time})
    db.session.commit()