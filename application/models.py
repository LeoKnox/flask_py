import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class Builder(db.Document):
    builder_id  =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30 )
    password    =   db.StringField( )

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def get_password(self, password):
        return check_password_hash(self.password, password)

class Room(db.Document):
    room_id     =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=50 )
    floor       =   db.StringField( max_length=50 )
    length      =   db.IntField()
    width       =   db.IntField()

class Dungeon(db.Document):
    builder_id  =   db.IntField()
    room_id     =   db.StringField( max_length=10 )