from app import db

class User(db.Model):
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