from config import Config

from flask import Flask
from flask_mail import Mail, Message 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os

app=Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)
mail=Mail(app)
migrate=Migrate(app, db)

from app import models, routes
