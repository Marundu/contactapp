from app.models import ContactDetails

from datetime import datetime

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactDetailsForm(FlaskForm):
    name=StringField('Name', validators=[DataRequired('Please enter your name'), Length(min=1, max=140)])
    email=StringField('Email', validators=[DataRequired('Please enter a valid email address'), Email()])
    phone_number=StringField('Phone Number', validators=[DataRequired('Please enter your phone number'), Length(min=1, max=20)])
    feedback=TextAreaField('Tell us what you think...', validators=[DataRequired('Say something, say something, baby'), Length(min=1, max=1000)])
    date_sent=StringField('Sent on', validators=[DataRequired()], default=datetime.utcnow())
    submit=SubmitField('Submit')

class UserForm(FlaskForm):
    name=StringField('Name', validators=[DataRequired('Please enter your name'), Length(min=1, max=140)])
    email=StringField('Email', validators=[DataRequired('Please enter a valid email address'), Email()])
    about_me=StringField('About me',validators=[DataRequired('Tell us a bit about yourself'), Length(min=1, max=300)])
