from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt, mail
from app.forms import Registration, Login, Edit, Add_Photo, email_reset_pass, reset_pass
from app.models import User, Photos
from flask_login import login_user, logout_user, current_user, login_required
import secrets, os
from PIL import Image
from flask_mail import Message

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/double-exposure/')
def double_exposure():
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "11", "12", "13", "14", "15", "16"]
    return render_template('double-exposure.html', x=x, enumerate=enumerate)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Registration()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def update_profile_picture(picture):
    name = secrets.token_hex(8)
    _, ext = os.path.splitext(picture.filename)
    profile_picture_name = name + ext
    path = os.path.join(app.root_path, 'static', 'profile pictures' , profile_picture_name)
    size = (125, 125)
    image = Image.open(picture)
    image.thumbnail(size)
    image.save(path)
    return profile_picture_name

@app.route('/account/edit', methods=['GET', 'POST'])
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
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='profile pictures/' + current_user.profile_picture)
    return render_template('edit.html', title='Edit Account', image=image, form=form)

@app.route('/account', methods=['GET'])
@login_required
def account():
    photo = Photos.query.filter_by(user_id=current_user.id).all()
    list = []
    for i in range(0,len(photo)):
        temp = photo[i].photo_link
        list.append(temp)
    form = Edit()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='profile pictures/' + current_user.profile_picture)
    return render_template('account.html', title='Edit Account', image=image, form=form, photo=list, enumerate=enumerate)

@app.route('/photo/new', methods=['GET', 'POST'])
@login_required
def new_photo():
    form = Add_Photo()
    if form.validate_on_submit():
        client = User.query.filter_by(email=form.client.data).first()
        photo = Photos(photo_name=form.name.data, photo_category=form.category.data, photo_link=form.link.data, client=client)
        db.session.add(photo)
        db.session.commit()
        flash('Image information added', 'info')
        return redirect(url_for('index'))
    return render_template('new_photo.html', title="New Photo", form=form)

def send_reset_email(user):
    token = user.reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset password pls click link:
{url_for('reset_password', token=token, _external=True)}

If you did not make request dw
'''
    mail.send(msg)

@app.route('/reset_password', methods=['GET', 'POST'])
def request_reset_email():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = email_reset_pass()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Email has been sent pls open', 'info')
        return redirect(url_for('login'))
    return render_template('request_reset.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_token(token)
    if user is None: #if not user
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('request_reset_email'))
    form = reset_pass()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()
        flash(f'Password for {user.username} updated!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_pass.html', title='Reset Password', form=form)