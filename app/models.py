from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    photos = db.relationship('Photos', backref='client', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(20), unique=True, nullable=False)
    photo_category = db.Column(db.String(20), nullable=False)
    photo_link = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Photos('{self.photo_name}','{self.photo_category}','{self.photo_link}')"