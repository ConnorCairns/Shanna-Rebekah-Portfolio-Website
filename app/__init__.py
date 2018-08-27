import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


#Flask and db setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#Encryption setup
app.config['SECRET_KEY'] = 'ihatecoursework'
bcrypt = Bcrypt(app)
#Login setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
#Mail setup
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('email_username')
app.config['MAIL_PASSWORD'] = os.environ.get('email_pass')
mail = Mail(app)

from app import routes