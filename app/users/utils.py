import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from app import mail
from flask import current_app, render_template

def update_profile_picture(picture):
    name = secrets.token_hex(8)
    _, ext = os.path.splitext(picture.filename)
    profile_picture_name = name + ext
    path = os.path.join(current_app.root_path, 'static', 'profile_pictures' , profile_picture_name)
    size = (125, 125)
    image = Image.open(picture)
    image.thumbnail(size)
    image.save(path)
    return profile_picture_name

def send_reset_email(user):
    token = user.reset_token()
    msg = Message('Password Reset Request', sender='Shanna Rebekah Photography', recipients=[user.email])
    msg.html = render_template("emails/password_reset.html", token=token )
    mail.send(msg)

def get_photo(photo, list):
    for i in range(0,len(photo)):
        temp = photo[i].photo_name
        list.append(temp)
    return list