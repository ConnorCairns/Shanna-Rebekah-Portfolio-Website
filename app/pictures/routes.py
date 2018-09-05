from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required
from app import db
from app.models import Photos, User
from app.pictures.forms import Add_Photo
from app.pictures.utils import s3_upload, save_pic, del_pic, s3_download
from sqlalchemy import and_

pictures = Blueprint('pictures', __name__)

@pictures.route('/photo/new', methods=['GET', 'POST'])
@login_required
@User.must_be_role("Admin")
def new_photo():
    form = Add_Photo()
    if form.validate_on_submit():
        client = User.query.filter_by(email=form.client.data).first_or_404()
        photo = Photos(photo_name=form.name.data, photo_category=form.category.data, client=client)
        db.session.add(photo)
        db.session.commit()
        save_pic(form.picture.data, form.name.data)
        s3_upload(form.name.data)
        del_pic(form.name.data)
        flash('Image information added', 'info')
        return redirect(url_for('pictures.new_photo'))
    return render_template('account/new_photo.html', title="New Photo", form=form)

@pictures.route('/picture/<jsdata>.JPG')
@login_required
def get_js_data(jsdata):
    user = Photos.query.filter(and_(Photos.photo_name==jsdata, Photos.user_id==current_user.id)).first_or_404()
    if user:
        s3_download(jsdata)
        return render_template('account/picture.html', data=jsdata)
    else:
        return render_template('errors/error_403.html'), 403