from db import db

def create_user(user: str, passw: str):
    query = """
        INSERT INTO users (username, password)
        VALUES (:user, :passw)
    """

    db.session.execute(query, {"user":user, "passw":passw})
