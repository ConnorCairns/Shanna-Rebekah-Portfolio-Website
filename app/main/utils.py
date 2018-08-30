from flask_mail import Message
from app import mail
from flask import render_template

def send_email(form):
    msg = Message(subject=form.title.data, sender='noreply@demo.com', recipients=['connor@connorcairns.xyz'])
    msg.html = render_template("emails/contact_request.html", name=f'{form.fname.data} {form.sname.data}', body=form.body.data )
    mail.send(msg)