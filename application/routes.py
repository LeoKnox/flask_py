from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
     return render_template("index.html", active_index = "active")

@app.route("/rooms")
def rooms():
    roomData = [{"RoomID":"0000","RoomName":"Entry","Length":5,"Width":5}]
    return render_template("rooms.html", active_rooms ="active", roomData = roomData)

@app.route("/register")
def register():
     return render_template("register.html")

@app.route("/login")
def login():
     return render_template("login.html")