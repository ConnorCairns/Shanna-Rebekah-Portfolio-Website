from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.main.forms import contact_form
from app.main.utils import send_email

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about/')
def about():
    return render_template('about.html')

@main.route('/contact/', methods=['GET','POST'])
def contact():
    form = contact_form()
    if form.validate_on_submit():
        send_email(form)
        flash(f'Email sent!', 'success')
        return redirect(url_for('main.index'))
    return render_template('contact.html', form=form)


@main.route('/double-exposure/')
def double_exposure():
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "11", "12", "13", "14", "15", "16"]
    return render_template('double-exposure.html', x=x, enumerate=enumerate)