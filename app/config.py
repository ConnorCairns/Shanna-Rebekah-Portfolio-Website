import os

class config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('shanna_db')
    SECRET_KEY = os.environ.get('shanna_secret_key')
    #6bcf0e1469bdd8f16d0ea63450c90b11
    MAIL_SERVER = 'smtp.googlemail.com'
    PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('email_username')
    MAIL_PASSWORD = os.environ.get('email_pass')