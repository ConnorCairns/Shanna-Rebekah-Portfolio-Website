from app import db, login_manager
from flask_login import UserMixin, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, abort
from functools import wraps

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    role = db.Column(db.String(10), nullable=False, default='Client')
    photos = db.relationship('Photos', backref='client', lazy=True)

    def reset_token(self, expire=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expire)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    @staticmethod
    def must_be_role(role):
        def must_be_role_decorator(func):
            @wraps(func)
            def role_checker(*args, **kwargs):
                if current_user.role != role:
                    return abort(403)
                else:
                    return func(*args, **kwargs)      
            return role_checker
        return must_be_role_decorator

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'username': self.username,
            'role': self.role,
            'photos': self.photos
        }

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.profile_picture}')"



class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(20), unique=True, nullable=False)
    photo_category = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Photos('{self.photo_name}','{self.photo_category}','{self.photo_link}')"

class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(20), unique=True, nullable=False)
    page_category = db.Column(db.String(20), nullable=False)
    page_text = db.Column(db.Text, nullable=False)
    images = db.relationship('PageImages', backref='page', lazy=True)

class PageImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(20), unique=True, nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'), nullable=False)

class Todo_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    