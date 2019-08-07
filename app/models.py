from app import db

from datetime import datetime

class ContactDetails(db.Model):

    __tablename__='contactdetails'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(140), index=True)
    email=db.Column(db.String(140), index=True)
    phone_number=db.Column(db.String(20), index=True)
    feedback=db.Column(db.Text(1000))
    date_sent=db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):

    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(140), index=True)
    email=db.Column(db.String(140), index=True)
    about_me=db.Column(db.String(300), index=True)
