from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
     return render_template("index.html")

@app.route("/rooms")
def rooms():
     return render_template("rooms.html")

@app.route("/register")
def register():
     return render_template("register.html")

@app.route("/login")
def login():
     return render_template("login.html")