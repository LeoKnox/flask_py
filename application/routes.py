from application import app, db
from flask import render_template

class Room(db.Document):
    room_id     =   db.IntField( unique=True )
    room_name   =   db.StringField( max_length =30 )
    length      =   db.IntField()
    width       =   db.IntField()
    pos_x       =   db.IntField()
    pos_y       =   db.IntField()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index="active")

@app.route("/dungeon")
def dungeon():
    info = Room.objects.all()
    return render_template("dungeon.html", dungeon="active", info=info)

@app.route("/room/")
@app.route("/room/<room_name>")
def room(room_name="Entry"):
    if not room_name:
        room_name="Entry"
    room_data = Room.objects.get(room_name=room_name)
    return render_template("room.html", room="active", info=room_data)

@app.route("/map")
def map():
    return render_template("map.html", map="active")

@app.route("/monsters")
def monsters():
    return render_template("monsters.html", monsters="active")

@app.route("/treasure")
def treasure():
    return render_template("treasure.html", treasure="active")