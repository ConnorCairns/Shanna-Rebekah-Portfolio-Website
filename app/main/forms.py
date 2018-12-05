from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, length, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models import Pages, PageImages

class contact_form(FlaskForm):
    fname = StringField("First Name", validators=[DataRequired(), length(min=2, max=35)])
    sname = StringField("Surname", validators=[DataRequired(), length(min=2, max=35)])
    email = StringField("Email", validators=[DataRequired(),Email()])
    title = StringField("Message Title", validators=[DataRequired(), length(min=2, max=50)])
    body = TextAreaField("Message", validators=[DataRequired(), length(min=2, max=2500)])
    submit = SubmitField("Submit")

class New_photoshoot(FlaskForm):
    name = StringField("Photoshoot Name", validators=[DataRequired(), length(min=2, max=20)])
    category = SelectField("Photoshoot Category", choices=[('portraits','Portraits'),('wedding','Wedding'),('still life','Still Life'),('the beauty of the struggles of society','The Beauty of the Struggles of Society'),('fashion','Fashion'),('food','Food')])
    text = TextAreaField("Photoshoot Description", validators=[DataRequired()])
    submit = SubmitField("Add Photoshoot")

    def validate_name(self, name):
        name = Pages.query.filter_by(page_name=str(name.data).lower()).first()
        if name:
            raise ValidationError('A photoshoot already exists with that name')

class Add_Photoshoot_Photo(FlaskForm):
    name = StringField("Image Name", validators=[DataRequired()])
    page = StringField("Page Name", validators=[DataRequired()])
    picture = FileField('Upload Photo', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField("Add photo")

    def validate_name(self, name):
        name = PageImages.query.filter_by(photo_name=str(name.data).lower()).first()
        if name:
            raise ValidationError('A photo already exists with that name')

    def validate_page(self, page):
        page = Pages.query.filter_by(page_name=(page.data).lower()).first()
        if page is None:
            raise ValidationError('No page exists with that name')