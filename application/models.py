import flask
from application import db

class Room(db.Document):
    room_id     =   db.IntField( unique=True )
    room_name   =   db.StringField( max_length =30 )
    length      =   db.IntField()
    width       =   db.IntField()
    pos_x       =   db.IntField()
    pos_y       =   db.IntField()