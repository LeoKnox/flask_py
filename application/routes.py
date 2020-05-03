from application import app
from flask import render_template, request

@app.route("/")
@app.route("/index")
def index():
     return render_template("index.html", active_index = "active")

@app.route("/rooms")
def rooms():
    roomData = [{"roomID":"0000","roomName":"Entry","length":5,"width":5},
                {"roomID":"0001","roomName":"Sentry","length":8,"width":6}]
    return render_template("rooms.html", active_rooms ="active", roomData = roomData)

@app.route("/edit_room", methods=["GET","POST"])
def edit_room():
    id = request.form['roomID']
    return render_template("edit_room.html", id = id)

@app.route("/register")
def register():
     return render_template("register.html")

@app.route("/login")
def login():
     return render_template("login.html")