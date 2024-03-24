from app import app
from flask import render_template, request, redirect
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

        if not users.login(username, password):
            return render_template("error.html", message="Wrong username or password")
        return redirect("/")