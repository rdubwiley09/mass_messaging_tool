from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired

class TextingForm(FlaskForm):
    number= StringField('Twilio Number', validators = [InputRequired("Please enter a number")])
    key = PasswordField('Twilio Key', validators = [InputRequired("Please enter your key")])
    textingList = FileField('Call List File', validators=[InputRequired("Please upload a file"),FileAllowed(['csv', 'CSVs only!'])])
    message = TextAreaField('Message Text', validators = [InputRequired("Please enter your message")])
    submit =  SubmitField('Submit')
