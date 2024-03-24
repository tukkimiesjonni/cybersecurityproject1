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
    session["user_name"] = username
    session["csrf_token"] = os.urandom(16).hex()
    return True

def create_user(user, passw):

    passw_hash = generate_password_hash(passw)

    query = text("""
        INSERT INTO users (name, password)
        VALUES (:user, :passw)
    """)

    db.session.execute(query, {"user":user, "passw":passw_hash})
    db.session.commit()

    return login(user, passw)


def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)