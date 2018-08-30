from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Photos
from app.users.forms import Registration, Login, Edit, email_reset_pass, reset_pass, search
from app.users.utils import update_profile_picture, send_reset_email
from wtforms.validators import ValidationError
from sqlalchemy import and_

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = Registration()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data.lower(), email=form.email.data.lower(), password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@users.route('/account', methods=['GET','POST'])
@login_required
def account():
    photo = Photos.query.filter_by(user_id=current_user.id).all()
    list = []
    for i in range(0,len(photo)):
        temp = photo[i].photo_link
        list.append(temp)
    form = Edit()
    search_form = search()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    if search_form.validate_on_submit():
        list = [] #needs to be here otherwise original photos stay on the page
        photo = Photos.query.filter(and_(Photos.photo_name.like("%" + search_form.search_query.data + "%"), Photos.user_id==current_user.id)).all()
        for i in range(0,len(photo)):
            temp = photo[i].photo_link
            list.append(temp)
    image = url_for('static', filename='profile pictures/' + current_user.profile_picture)
    return render_template('account.html', title='Edit Account', image=image, form=form, photo=list, enumerate=enumerate, search_form=search_form)

@users.route('/reset_password', methods=['GET', 'POST'])
def request_reset_email():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = email_reset_pass()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Email has been sent pls open', 'info')
        return redirect(url_for('users.login'))
    return render_template('request_reset.html', title='Reset Password', form=form)

@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_token(token)
    if user is None: #if not user
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('users.request_reset_email'))
    form = reset_pass()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()
        flash(f'Password for {user.username} updated!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_pass.html', title='Reset Password', form=form)

@users.route('/account/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = Edit()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture = update_profile_picture(form.profile_picture.data)
            current_user.profile_picture = picture
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Account information updated', 'info')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='profile pictures/' + current_user.profile_picture)
    return render_template('edit.html', title='Edit Account', image=image, form=form)