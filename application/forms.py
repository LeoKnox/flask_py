from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FormField, FieldList, SelectField
from wtforms.validators import DataRequired, ValidationError

class DoorForm(FlaskForm):
    #wall        =   IntegerField("Wall")
    position    =   SelectField("Position", choices=[(1,3),(2,4)])

class CreateRoomForm(FlaskForm):
    room_name   =   StringField("Room Name", validators=[DataRequired()])
    length      =   IntegerField("Length", validators=[DataRequired()])
    width       =   IntegerField("Width", validators=[DataRequired()])
    pos_x       =   IntegerField("X Position", validators=[DataRequired()])
    pos_y       =   IntegerField("Y Position", validators=[DataRequired()])
    doors       =   FieldList(FormField(DoorForm))
    submit      =   SubmitField("Submit")