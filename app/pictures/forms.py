from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed

class Add_Photo(FlaskForm):
    name = StringField("Image Name", validators=[DataRequired()])
    category = StringField("Image Category", validators=[DataRequired()])
    client = StringField("Client Email", validators=[DataRequired(), Email()])
    picture = FileField('Upload Photo', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Add photo")
