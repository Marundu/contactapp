import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or '73pyr@njw%>4<0sdc8m^'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'contactdetails.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
