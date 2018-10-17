from app.models import ContactDetails

from datetime import datetime

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactDetailsForm(FlaskForm):
    name=StringField('Name', validators=[DataRequired(), Length(min=1, max=140)])
    email=StringField('Email', validators=[DataRequired(), Email()])
    phone_number=StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=20)])
    feedback=TextAreaField('Tell us what you think...', validators=[DataRequired(), Length(min=1, max=250)])
    date_sent=StringField('Sent on', validators=[DataRequired()], default=datetime.utcnow())
    submit=SubmitField('Submit')
