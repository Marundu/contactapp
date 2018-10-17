from app import db

from datetime import datetime

class ContactDetails(db.Model):
    
    __tablename__='contactdetails'    
    
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(140), index=True)
    email=db.Column(db.String(140), index=True)
    phone_number=db.Column(db.String(20), index=True)
    feedback=db.Column(db.String(250))
    date_sent=db.Column(db.DateTime, default=datetime.utcnow)
