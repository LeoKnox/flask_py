import flask
from application import db

class Room(db.Document):
    room_name   =   db.StringField( max_length =30, unique=True )
    length      =   db.IntField()
    width       =   db.IntField()
    pos_x       =   db.IntField()
    pos_y       =   db.IntField()
    doors       =   db.StringField()