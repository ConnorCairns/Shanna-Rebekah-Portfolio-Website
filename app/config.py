import os

class config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('shanna_db')
    SECRET_KEY = os.environ.get('shanna_secret_key')
    MAIL_SERVER = 'smtp.googlemail.com'
    PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('email_username')
    MAIL_PASSWORD = os.environ.get('email_pass')
    RECAPTCHA_PUBLIC_KEY = '6LfTRIoUAAAAAHAOHJFr2xahNSNDveEi70_Zm1MF'
    RECAPTCHA_PRIVATE_KEY = '6LfTRIoUAAAAAN1Q2w8Cz8mx0f8a1UvkCVlLfkZ1'
    RECAPTCHA_DATA_ATTRS = {'size': 'compact normal'}