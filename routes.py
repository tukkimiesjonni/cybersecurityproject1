from app import app
from flask import render_template, request, redirect


@app.route("/")
def home():
    return render_template("home.html")