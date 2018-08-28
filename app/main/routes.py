from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about/')
def about():
    return render_template('about.html')


@main.route('/contact/')
def contact():
    return render_template('contact.html')


@main.route('/double-exposure/')
def double_exposure():
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "11", "12", "13", "14", "15", "16"]
    return render_template('double-exposure.html', x=x, enumerate=enumerate)