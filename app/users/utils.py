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
    msg = Message('Password Reset Request', sender=("Shanna Rebekah Photography", "shannarebekahphotography@gmail.com"), recipients=[user.email])
    msg.html = render_template("emails/password_reset.html", token=token )
    mail.send(msg)

def get_photo(photo, photo_list):
    for photo in photo:
        temp = photo.photo_name
        photo_list.append(temp)
    return photo_list

def get_todo(todos_object, todos, ids):
    for todo in todos_object:
        temp = todo.todo
        todos.append(temp)
        temp = todo.id
        ids.append(temp)
    return todos, ids

def get_admin_page(usernames, emails, last_logins, photo_name, photo_category, clients, users, photos):
    for user in users:
        usernames.append(user.username)
        emails.append(user.email)
        last_logins.append(user.last_login)
    for photo in photos:
        photo_name.append(photo.photo_name)
        photo_category.append(photo.photo_category)
        clients.append(photo.client.email)
    return usernames, emails, last_logins, photo_name, photo_category, clients