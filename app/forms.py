from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email

# a Python class called ContactForm to represent your form using the various field types and validators available to you in Flask-WTF. Your form should have a text field for name, email, subject and a text area for a message.

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    email = StringField('Email',validators=[InputRequired(), Email()])
    subject = StringField('Subject',validators=[InputRequired()])
    message = StringField('Messsage',validators=[InputRequired()])