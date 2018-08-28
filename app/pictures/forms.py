from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class Add_Photo(FlaskForm):
    name = StringField("Image Name", validators=[DataRequired()])
    category = StringField("Image Category", validators=[DataRequired()])
    link = StringField("Image Link", validators=[DataRequired()])
    client = StringField("Client Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Add photo")
