from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required
from app import db
from app.models import Photos, User
from app.pictures.forms import Add_Photo
from app.pictures.utils import s3_upload, save_pic, del_pic

pictures = Blueprint('pictures', __name__)

@pictures.route('/photo/new', methods=['GET', 'POST'])
@login_required
@User.must_be_role("Admin")
def new_photo():
    form = Add_Photo()
    if form.validate_on_submit():
        client = User.query.filter_by(email=form.client.data).first()
        link = f'https://s3.eu-west-2.amazonaws.com/shanna-rebekah-photography/{form.name.data}.JPG'
        photo = Photos(photo_name=form.name.data, photo_category=form.category.data, photo_link=link, client=client)
        db.session.add(photo)
        db.session.commit()
        save_pic(form.picture.data, form.name.data)
        s3_upload(form.name.data)
        del_pic(form.name.data)
        flash('Image information added', 'info')
        return redirect(url_for('pictures.new_photo'))
    return render_template('new_photo.html', title="New Photo", form=form)