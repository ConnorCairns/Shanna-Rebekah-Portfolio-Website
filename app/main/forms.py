from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length, Email

class contact_form(FlaskForm):
    fname = StringField("First Name", validators=[DataRequired(), length(min=2, max=35)])
    sname = StringField("Surname", validators=[DataRequired(), length(min=2, max=35)])
    email = StringField("Email", validators=[DataRequired(),Email()])
    title = StringField("Message Title", validators=[DataRequired(), length(min=2, max=50)])
    body = TextAreaField("Message", validators=[DataRequired(), length(min=2, max=2500)])
    submit = SubmitField("Submit")