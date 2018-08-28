import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from app import mail
from flask import current_app

def update_profile_picture(picture):
    name = secrets.token_hex(8)
    _, ext = os.path.splitext(picture.filename)
    profile_picture_name = name + ext
    path = os.path.join(current_app.root_path, 'static', 'profile pictures' , profile_picture_name)
    size = (125, 125)
    image = Image.open(picture)
    image.thumbnail(size)
    image.save(path)
    return profile_picture_name

def send_reset_email(user):
    token = user.reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset password pls click link:
{url_for('users.reset_password', token=token, _external=True)}

If you did not make request dw
'''
    mail.send(msg)
