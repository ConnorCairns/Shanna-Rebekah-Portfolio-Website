from flask_mail import Message
from app import mail
from flask import render_template

def send_email(form):
    msg = Message(subject=form.title.data, sender=("Shanna Rebekah Photography", "shannarebekahphotography@gmail.com"), recipients=['shannarebekahphotography@gmail.com'])
    msg.html = render_template("emails/contact_request.html", name=f'{form.fname.data} {form.sname.data}', email=form.email.data ,body=form.body.data )
    mail.send(msg)