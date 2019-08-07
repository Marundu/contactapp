import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or '73pyr@njw%>4<0sdc8m^'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'contactdetails.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    # Email settings 

    # EMAIL_USE_SMTP=True
    MAIL_SERVER='smtp.sendgrid.net'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    # MAIL_USE_SSL=True 
    MAIL_USERNAME='apikey'
    MAIL_PASSWORD=os.environ.get('SENDGRID_API_KEY')
    RECIPIENT_EMAIL=os.environ.get('RECIPIENT_EMAIL')
    # ADMINS=['chipomwitu88@gmail.com']
