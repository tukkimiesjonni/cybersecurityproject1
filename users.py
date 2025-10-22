import os
from db import execute_query
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash


def login(username, password):
    # A03 Injection
    # The following query is vulnerable to SQL injection as it directly inserts the username into the query
    # Proper query and the execute_query call is commented out below

    # Injection vulnerable code starts here:
    query = f"""
        SELECT password, id 
        FROM users 
        WHERE name = '{username}'
    """

    result = execute_query(query, fetch=True)
    if not result:
        return False
    # Injection vulnerable code ends here

    # # Injection safe code starts here:
    # query = """
    #     SELECT password, id 
    #     FROM users 
    #     WHERE name = ?
    # """
    # result = execute_query(query, (username,), fetch=True)
    # if not result:
    #     return False
    # # Injection safe code ends here

    # Function for logging in user with plaintext password starts here:
    user = result[0]
    hashed_password, user_id = user["password"], user["id"]

    stored_plaintext = hashed_password
    if stored_plaintext == password:
        session["user_id"] = user_id
        session["username"] = username
        return True
    else:
        return False
    # Function for logging in user with plaintext password ends here


    # # Function for logging in user with hashed password starts here:
    # if not check_password_hash(hashed_password, password):
    #     return False

    # session["user_id"] = user_id
    # session["username"] = username
    # # session["csrf_token"] = os.urandom(16).hex()
    # return True
    # # Function for logging in user with hashed password ends here


def check_if_user_exists(username):
    query = """
        SELECT COUNT(*) AS count FROM users
        WHERE name = ?
    """

    result = execute_query(query, (username,), fetch=True)
    return result[0]["count"] != 0


def create_user(username, password):
    # A02 Cryptographic Failures
    # When creating user, password should be hashed before storing in DB, in this app it is stored as plain text
    # To store hashed password, we could use the following line that stores the password with hashing function from werkzeug

    # Password stored as plain text:
    password_hash = password

    # Password stored as hashed value:
    # password_hash = generate_password_hash(password)

    query = """
        INSERT INTO users (name, password)
        VALUES (?, ?)
    """

    execute_query(query, (username, password_hash))

    return login(username, password)


def get_user_id():
    username = session.get("username")

    query = """
        SELECT id FROM users
        WHERE name = ?
    """

    result = execute_query(query, (username,), fetch=True)
    return result[0]["id"] if result else None


# CSRF protection function disabled and commented out in various places
# def check_csrf():
#     if session["csrf_token"] != request.form.get("csrf_token"):
#         abort(403)
