import os
from hashlib import sha256
from db import db
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def login(username, password):
    query = text("""
        SELECT password, id 
        FROM users 
        WHERE name=:username
    """)

    result = db.session.execute(query, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    
    session["user_id"] = user[0]
    session["username"] = username
    session["csrf_token"] = os.urandom(16).hex()
    return True


def check_if_user_exists(username):
    query = text("""
        SELECT COUNT(*) FROM users
        WHERE name=:username
    """)

    result = db.session.execute(query, {"username":username})
    if result.fetchone()[0] != 0:
        return True
    return False


def create_user(username, password):

    password_hash = generate_password_hash(password)

    query = text("""
        INSERT INTO users (name, password)
        VALUES (:username, :password)
    """)

    db.session.execute(query, {"username":username, "password":password_hash})
    db.session.commit()

    return login(username, password)


def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)