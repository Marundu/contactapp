from app import app, db
from app.forms import ContactDetailsForm
from app.models import ContactDetails

from datetime import datetime

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, login_required, logout_user


@app.route('/', methods=['GET', 'POST'])
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form=ContactDetailsForm()
    if form.validate_on_submit():
        contactdetails=ContactDetails(
            name=form.name.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            feedback=form.feedback.data
            )

        db.session.add(contactdetails)
        db.session.commit()
        flash('Thank you for getting in touch with us! We will get back to you right after our nth juice.')

        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    pass


@app.route('/admin/delete', methods=['GET', 'POST'])
@login_required
def delete_record(): # inappropriate
    pass # full-text search?


@app.route('/admin/add_user', methods=['GET', 'POST'])
@login_required
def add_user(): # admin user or user who can only view records
    pass


@app.route('/view_contacts', methods=['GET', 'POST'])
@login_required
def view_contacts():
    pass
