from app import app
from flask import render_template, request, redirect, session
import users
import threads


@app.route("/")
def home():
    thread_list = threads.get_threads()
    return render_template("home.html", threads=thread_list)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if len(username) < 1:
            return render_template("message.html", message="Username cannot be empty")
        if len(username) > 20:
            return render_template("message.html", message="Username must be under 20 characters")
        if len(password) < 1:
            return render_template("message.html", message="Password cannot be empty")
        if len(password) > 100:
            return render_template("message.html", message="Password must be under 100 characters")
        
        if users.check_if_user_exists(username):
            return render_template("message.html", message="Username is already taken")
        
        if not users.create_user(username, password):
            return render_template("message.html", message="Signing up failed")
        
        return redirect("/")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        users.check_csrf()
        username = request.form["username"]
        password = request.form["password"]

        if users.login(username, password):
            return redirect("/")
        return render_template("message.html", message="Wrong username or password")
    

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/new_thread", methods=["GET", "POST"])
def new_thread():
    if request.method == "GET":
        return render_template("new_thread.html")
    
    if request.method == "POST":
        users.check_csrf()
        title = request.form["title"]
        content = request.form["content"]
        if threads.create_thread(title, content):
            return render_template("message.html", message="Thread succesfully created")
        else:
            return render_template("message.html", message="Something went wrong")
        

@app.route("/thread/<int:id>", methods=["GET", "POST"])
def thread_view(id):
    if request.method == "GET":
        thread = threads.get_thread(id)
        comments = threads.get_comments(id)
        return render_template("thread.html", content=thread, id=id, comments=comments)


@app.route("/upvote/<int:id>", methods=["GET", "POST"])
def upvote(id):
    if request.method == "POST":
        threads.upvote(id)
        users.check_csrf()
        thread = threads.get_thread(id)
        comments = threads.get_comments(id)
        return render_template("thread.html", content=thread, id=id, comments=comments)


@app.route("/downvote/<int:id>", methods=["GET", "POST"])
def downvote(id):
    if request.method == "POST":
        users.check_csrf()
        threads.downvote(id)
        thread = threads.get_thread(id)
        comments = threads.get_comments(id)
        return render_template("thread.html", content=thread, id=id, comments=comments)
    

@app.route("/new_comment/<int:id>", methods=["GET", "POST"])
def new_comment(id):
    if request.method == "POST":
        users.check_csrf()
        user = users.get_user_id()
        comment_content = request.form["comment-content"]
        threads.new_comment(id, user, comment_content)
        thread = threads.get_thread(id)
        comments = threads.get_comments(id)
        return render_template("thread.html", content=thread, id=id, comments=comments)