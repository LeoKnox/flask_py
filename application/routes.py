from application import app, db
from flask import render_template, request, redirect, flash, url_for
from application.models import Builder, Room, Dungeon
from application.forms import BuilderForm, RegisterForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", active_index = "active")

@app.route("/rooms")
def rooms():
    #roomData = [{"roomID":"0000","roomName":"Entry","length":5,"width":5},
    #            {"roomID":"0001","roomName":"Sentry","length":8,"width":6}]
    roomData = Room.objects.order_by("+roomID")
    print (roomData)
    return render_template("rooms.html", active_rooms ="active", roomData = roomData)

@app.route("/edit_room", methods=["GET","POST"])
def edit_room():
    roomID = request.form.get('roomID')
    roomName = request.form.get('roomName')
    length = request.form.get('length')
    width = request.form.get('width')
    builder_id=1
    if roomID:
        if Dungeon.objects(builder_id=builder_id,roomID=roomID):
            flash(f"Already added room {roomName}", "negative")
            return redirect(url_for("rooms"))
        else:
            Dungeon(builder_id=builder_id,roomID=roomID)
            flash(f'Room added in {roomName}', "positive")

    return render_template("edit_room.html", roomID = roomID)

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        builder_id  =   Builder.objects.count()
        builder_id  += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        builder = Builder(builder_id=builder_id,email=email,first_name=first_name,last_name=last_name)
        builder.set_password(password)
        builder.save()
        flash('Successfully created', 'positive')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = BuilderForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        builder = Builder.objects(email=email).first()
        print(builder.get_password(password))
        if builder and builder.get_password(password):
            flash(f"{builder.first_name}, You are logged in.", "positive")
            return redirect("/index")
        else:
            flash("Sorry, please try again or register.", "negative")
    return render_template("login.html", form=form, login="active")

@app.route("/show_room"):
def show_room():
    return render_template("show_room.html")

@app.route("/about")
def about():
    return render_template("about.html", about="active")

@app.route("/builder")
def builder():
    #Builder(builder_id=1, first_name="Kiki", last_name="Killer", email="kikikiller@dungeon.com", password="kiki1234").save()
    #Builder(builder_id=2, first_name="Kylu", last_name="Kastle", email="kylukastle@dungeon.com", password="kylu1234").save()
    builders = Builder.objects.all()
    return render_template("builders.html", builders = builders)