from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class CreateRoomForm(FlaskForm):
    room_name   =   StringField("Room Name", validator=[DataRequired()])
    length      =   IntegerField("Length", validator=[DataRequired()])
    width       =   IntegerField("Width", validator=[DataRequired()])
    pos_x       =   IntegerField("X Position", validator=[DataRequired()])
    pos_y       =   IntegerField("Y Position", validator=[DataRequired()])