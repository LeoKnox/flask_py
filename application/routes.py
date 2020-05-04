from application import app, db
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

class Builder(db.Document):
    builder_id  =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30 )
    password    =   db.StringField( max_length=30 )

@app.route("/builder")
def builder():
    #Builder(builder_id=1, first_name="Kiki", last_name="Killer", email="kikikiller@dungeon.com", password="kiki1234").save()
    #Builder(builder_id=2, first_name="Kylu", last_name="Kastle", email="kylukastle@dungeon.com", password="kylu1234").save()
    builders = Builder.objects.all()
    return render_template("builders.html", builders = builders)