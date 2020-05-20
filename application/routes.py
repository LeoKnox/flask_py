from application import app, db, mycol
from application.models import Room
from application.forms import CreateRoomForm
from flask import render_template, request

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index="active")

@app.route("/dungeon")
def dungeon():
    info = Room.objects.all()
    return render_template("dungeon.html", dungeon="active", info=info)

@app.route("/room/", methods=["GET", "POST"])
@app.route("/room/<room_name>", methods=["GET", "POST"])
def room(room_name="Entry"):
    if not room_name:
        room_name="Entry"
    room_data = Room.objects.get(room_name=room_name)
    form = CreateRoomForm()
    if form.validate_on_submit():
        print("aaaaaa")
        room_name   =   form.room_name.data
        length      =   form.length.data
        width       =   form.width.data
        pos_x       =   form.pos_x.data
        pos_y       =   form.pos_y.data
        room = Room(room_name=room_name,length=length,width=width,pos_x=pos_x,pos_y=pos_y)

    room.save()

    return render_template("room.html", room="active", info=room_data, form=form)

@app.route("/map")
def map():
    x = 'Entry'
    y = {'room_name':x}
    newvalues = {"$set": {"pos_x":5,"pos_y":5}}
    z = mycol.update_many(y,newvalues)
    return render_template("map.html", map="active")

@app.route("/monsters")
def monsters():
    return render_template("monsters.html", monsters="active")

@app.route("/treasure")
def treasure():
    return render_template("treasure.html", treasure="active")