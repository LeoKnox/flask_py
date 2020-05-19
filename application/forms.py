from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class CreateRoomForm(FlaskForm):
    room_name   =   StringField("Room Name", validators=[DataRequired()])
    length      =   IntegerField("Length", validators=[DataRequired()])
    width       =   IntegerField("Width", validators=[DataRequired()])
    pos_x       =   IntegerField("X Position", validators=[DataRequired()])
    pos_y       =   IntegerField("Y Position", validators=[DataRequired()])
    submit      =   SubmitField("Submit")