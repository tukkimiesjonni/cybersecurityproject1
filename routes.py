from flask import render_template, request, redirect, session
from app import app, limiter
import users
import threads
import logging

logger = logging.getLogger(__name__)


@app.route("/")
def home():
    thread_list = threads.get_threads()
    sorted_thread_list = sorted(thread_list, key=lambda x: x[4], reverse=True)

    logger.info(f"Home page accessed by IP: {request.remote_addr}")

    return render_template("home.html", threads=sorted_thread_list)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        logger.info(f"Registration page viewed by IP: {request.remote_addr}")
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        logger.info(f"Registration attempt for username='{username}' from {request.remote_addr}")

        if len(username) < 1:
            logger.warning("Registration failed: empty username")
            return render_template("message.html", message="Username cannot be empty")

        if len(username) > 20:
            logger.warning("Registration failed: username too long")
            return render_template("message.html", message="Username must be under 20 characters")

        if len(password) < 1:
            logger.warning("Registration failed: empty password")
            return render_template("message.html", message="Password cannot be empty")

        if len(password) > 100:
            logger.warning("Registration failed: password too long")
            return render_template("message.html", message="Password must be under 100 characters")

        if users.check_if_user_exists(username):
            logger.warning(f"Registration failed: username '{username}' already exists")
            return render_template("message.html", message="Username is already taken")

        if not users.create_user(username, password):
            logger.error(f"Registration error for username='{username}'")
            return render_template("message.html", message="Signing up failed")

        logger.info(f"User '{username}' successfully registered.")
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
# A07 Identification and Authentication Failures
# Uncomment to enable rate limiting on login to prevent brute-force attacks
# @limiter.limit("5 per minute")
def login():
    if request.method == "GET":
        logger.info(f"Login page viewed by IP: {request.remote_addr}")
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.login(username, password):
            logger.info(f"User '{username}' successfully logged in from IP: {request.remote_addr}")
            return redirect("/")

        else:
            logger.warning(f"Failed login attempt for user '{username}' from IP: {request.remote_addr}")
            return render_template("message.html", message="Wrong username or password")


@app.route("/logout")
def logout():
    username = session.get("username", "Guest")
    logger.info(f"User '{username}' logged out from IP: {request.remote_addr}")

    del session["username"]
    
    return redirect("/")


@app.route("/new_thread", methods=["GET", "POST"])
def new_thread():
    if request.method == "GET":
        logger.info(f"New thread form viewed by user='{session.get('username', 'Guest')}'")
        return render_template("new_thread.html")

    if request.method == "POST":
        # users.check_csrf()
        title = request.form["title"]
        content = request.form["content"]
        logger.info(f"Thread creation attempt by '{session.get('username', 'Guest')}' with title='{title}'")

        if threads.create_thread(title, content):
            logger.info(f"Thread '{title}' successfully created by '{session.get('username', 'Guest')}'")
            return redirect("/")

        else:
            logger.error(f"Thread creation failed for user='{session.get('username', 'Guest')}'")
            return render_template("message.html", message="Something went wrong")


@app.route("/thread/<int:id>", methods=["GET", "POST"])
def thread_view(id):
    if request.method == "GET":
        logger.info(f"Thread #{id} viewed by user='{session.get('username', 'Guest')}'")
        thread = threads.get_thread(id)
        comments = threads.get_comments(id)
        votes = threads.count_votes(id)
        return render_template("thread.html", content=thread, id=id, comments=comments, votes=votes)


@app.route("/upvote/<int:id>", methods=["GET", "POST"])
def upvote(id):
    thread = threads.get_thread(id)
    comments = threads.get_comments(id)
    votes = threads.count_votes(id)

    if request.method == "GET":
        return render_template("thread.html", content=thread, id=id, comments=comments, votes=votes)

    if request.method == "POST":
        # users.check_csrf()
        logger.info(f"User '{session.get('username', 'Guest')}' upvoted thread #{id}")
        threads.upvote(id)
        return render_template("thread.html", content=thread, id=id, comments=comments, votes=votes)


@app.route("/downvote/<int:id>", methods=["GET", "POST"])
def downvote(id):
    thread = threads.get_thread(id)
    comments = threads.get_comments(id)
    votes = threads.count_votes(id)

    if request.method == "GET":
        return render_template("thread.html", content=thread, id=id, coments=comments, votes=votes)

    if request.method == "POST":
        # users.check_csrf()
        logger.info(f"User '{session.get('username', 'Guest')}' downvoted thread #{id}")
        threads.downvote(id)
        return render_template("thread.html", content=thread, id=id, comments=comments, votes=votes)
    

@app.route("/new_comment/<int:id>", methods=["GET", "POST"])
def new_comment(id):
    # users.check_csrf()
    user = users.get_user_id()
    comment_content = request.form["comment-content"]
    logger.info(f"User '{session.get('username', 'Guest')}' commented on thread #{id}: '{comment_content[:30]}...'")

    threads.new_comment(id, user, comment_content)
    thread = threads.get_thread(id)
    comments = threads.get_comments(id)
    votes = threads.count_votes(id)

    if request.method == "GET":
        return render_template("thread.html", content=thread, id=id, comments=comments, votes=votes)

    if request.method == "POST":
        # users.check_csrf()
        return render_template("thread.html", content=thread, id=id, comments=comments, votes=votes)
