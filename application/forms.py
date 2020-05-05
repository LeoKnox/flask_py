from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class BuilderForm(FlaskForm):
    email       =   StringField("Email", validators=[DataRequired()])
    password    =   StringField("Password", validators=[DataRequired()])
    remember_me =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")

class RegisterForm(FlaskForm):
    Email       =   StringField("Email", validators=[DataRequired()])
    password    =   StringField("Password", validators=[DataRequired()])
    password_confirm    =   StringField("Password", validators=[DataRequired()])
    first_name  =   StringField("First Name", validators=[DataRequired()])
    last_name   =   StringField("Last Name", validators=[DataRequired()])
    submit      =   SubmitField("Register Now")