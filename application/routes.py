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
    print(room_name)
    info = [
        {"room_name":"Entry","length":5,"width":5},
        {"room_name":"Storage","length":9,"width":7},
        {"room_name":"Insanity","length":8,"width":12}
    ]
    room_data = {"room_name":"Entry", "length":5, "width":5}
    room_data = next(item for item in info if item["room_name"] == room_name)
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