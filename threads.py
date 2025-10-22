from datetime import datetime
from db import execute_query
from users import get_user_id


def get_timestamp():
    return datetime.now()


def create_thread(title, content):
    user_id = get_user_id()
    time = get_timestamp()

    query = """
        INSERT INTO threads (user_id, title, content, published)
        VALUES (?, ?, ?, ?)
    """
    
    execute_query(query, (user_id, title, content, time))
    print("Thread added")
    return True


def get_thread_id(thread):
    query = """
        SELECT id FROM threads
        WHERE title = ?
    """
    result = execute_query(query, (thread,), fetch=True)
    return result[0]["id"] if result else None


def add_comment(thread, comment):
    time = get_timestamp()
    thread_id = get_thread_id(thread)
    user_id = get_user_id()

    query = """
        INSERT INTO comments (user_id, thread_id, comment, published)
        VALUES (?, ?, ?, ?)
    """
    
    execute_query(query, (user_id, thread_id, comment, time))


def get_threads():
    query = """
        SELECT threads.id, users.name, threads.title, threads.content, threads.published
        FROM users
        JOIN threads ON users.id = threads.user_id
        ORDER BY threads.published DESC
    """
    return execute_query(query, fetch=True)


def get_thread(thread_id):
    query = """
        SELECT users.name, threads.title, threads.content, threads.published
        FROM users
        JOIN threads ON users.id = threads.user_id
        WHERE threads.id = ?
    """
    result = execute_query(query, (thread_id,), fetch=True)
    return result[0] if result else None


def upvote(thread_id):
    query = """
        INSERT INTO votes (thread_id, vote)
        VALUES (?, 1)
    """
    execute_query(query, (thread_id,))


def downvote(thread_id):
    query = """
        INSERT INTO votes (thread_id, vote)
        VALUES (?, 0)
    """
    execute_query(query, (thread_id,))


def count_votes(thread_id):
    query_upvotes = """
        SELECT COUNT(*) AS count FROM votes
        WHERE thread_id = ? AND vote = 1
    """

    query_downvotes = """
        SELECT COUNT(*) AS count FROM votes
        WHERE thread_id = ? AND vote = 0
    """

    upvote_result = execute_query(query_upvotes, (thread_id,), fetch=True)
    downvote_result = execute_query(query_downvotes, (thread_id,), fetch=True)

    upvote_amount = upvote_result[0]["count"] if upvote_result else 0
    downvote_amount = downvote_result[0]["count"] if downvote_result else 0

    net_votes = upvote_amount - downvote_amount
    print(net_votes)
    return net_votes


def new_comment(thread_id, user_id, comment):
    if comment.strip() != "":

        query = """
            INSERT INTO comments (thread_id, user_id, comment)
            VALUES (?, ?, ?)
        """
        
        execute_query(query, (thread_id, user_id, comment))


def get_comments(thread_id):
    query = """
        SELECT users.name, comments.comment
        FROM comments
        INNER JOIN users ON comments.user_id = users.id
        WHERE comments.thread_id = ?
        ORDER BY comments.id ASC
    """
    return execute_query(query, (thread_id,), fetch=True)
