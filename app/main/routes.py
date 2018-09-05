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

# portraits
@main.route('/portraits/')
def portraits():
    return render_template('portraits/portraits.html')

@main.route('/portraits/disguise')
def portraits_disguise():
    return render_template('portraits/disguise.html')

@main.route('/portraits/something')
def portraits_something():
    return render_template('portraits/something.html')

@main.route('/portraits/somethingelse')
def portraits_somethingelse():
    return render_template('portraits/somethingelse.html')

@main.route('/portraits/frustration')
def portraits_frustration():
    return render_template('portraits/frustration.html')

@main.route('/wedding/')
def wedding():
    return render_template('coming_soon.html')

@main.route('/still life/')
def still_life():
    return render_template('coming_soon.html')

@main.route('/family/')
def family():
    return render_template('coming_soon.html')

@main.route('/fashion/')
def fashion():
    return render_template('coming_soon.html')

@main.route('/something/')
def something():
    return render_template('coming_soon.html')