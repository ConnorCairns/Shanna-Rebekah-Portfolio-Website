from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models import Photos, User

class Add_Photo(FlaskForm):
    name = StringField("Image Name", validators=[DataRequired()])
    category = SelectField("Image Category", choices=[('portraits','Portraits'),('wedding','Wedding'),('still life','Still Life'),('family','Family'),('fashion','Fashion'),('something','Something')])
    client = StringField("Client Email", validators=[DataRequired(), Email()])
    picture = FileField('Upload Photo', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField("Add photo")
            
    def validate_client(self, client):
        print(client)
        test = User.query.filter_by(email=(client.data).lower()).first()
        if test is None:
            raise ValidationError('There is no client with that email')

    def validate_name(self, name):
        name = Photos.query.filter_by(photo_name=(name.data).lower()).first()
        if name:
            raise ValidationError('A photo already exists with that name')


