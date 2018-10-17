# export FLASK_APP=contact.py

from app import app, db

from app.models import ContactDetails

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'ContactDetails': ContactDetails}
