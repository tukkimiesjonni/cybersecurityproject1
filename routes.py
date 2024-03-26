from app import app
from flask import render_template, request, redirect, session
import users


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        #users.check_csrf()

        username = request.form["username"]
        password = request.form["password"]

        if len(username) < 1:
            return render_template("error.html", message="Username cannot be empty")
        if len(username) > 20:
            return render_template("error.html", message="Username must be under 20 characters")
        if len(password) < 1:
            return render_template("error.html", message="Password cannot be empty")
        if len(password) > 100:
            return render_template("error.html", message="Password must be under 100 characters")
        
        if users.check_if_user_exists(username):
            return render_template("error.html", message="Username is already taken")
        
        if not users.create_user(username, password):
            return render_template("error.html", message="Signing up failed")
        
        return redirect("/")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.login(username, password):
            return redirect("/")
        return render_template("error.html", message="Wrong username or password")
    

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")