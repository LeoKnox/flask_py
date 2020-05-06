from application import app, db
from flask import render_template, request, redirect, flash
from application.models import Builder, Room, Dungeon
from application.forms import BuilderForm, RegisterForm

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

@app.route("/login", methods=['GET','POST'])
def login():
    form = BuilderForm()
    if form.validate_on_submit():
        if request.form.get("email") == "kikikiller@dungeon.com":
            flash("You are logged in.", "positive")
            return redirect("/index")
        else:
            flash("Sorry, please try again or register.", "negative")
    return render_template("login.html", form=form, login="active")

@app.route("/about")
def about():
    return render_template("about.html", about="active")

@app.route("/builder")
def builder():
    #Builder(builder_id=1, first_name="Kiki", last_name="Killer", email="kikikiller@dungeon.com", password="kiki1234").save()
    #Builder(builder_id=2, first_name="Kylu", last_name="Kastle", email="kylukastle@dungeon.com", password="kylu1234").save()
    builders = Builder.objects.all()
    return render_template("builders.html", builders = builders)