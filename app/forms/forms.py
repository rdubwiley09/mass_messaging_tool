from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(FlaskForm):
    username = StringField('User Name', validators = [InputRequired("Please enter a username")])
    password = PasswordField('Password', validators = [InputRequired("Please enter a password")])
    submit =  SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('User Name', validators = [InputRequired("Please enter a username")])
    password = PasswordField('Password', validators = [InputRequired("Please enter a password")])
    submit =  SubmitField('Register')
