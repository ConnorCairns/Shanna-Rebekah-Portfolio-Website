from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required
from app import db
from app.models import Photos
from app.pictures.forms import Add_Photo

pictures = Blueprint('pictures', __name__)

@pictures.route('/photo/new', methods=['GET', 'POST'])
@login_required
def new_photo():
    form = Add_Photo()
    if form.validate_on_submit():
        client = User.query.filter_by(email=form.client.data).first()
        photo = Photos(photo_name=form.name.data, photo_category=form.category.data, photo_link=form.link.data, client=client)
        db.session.add(photo)
        db.session.commit()
        flash('Image information added', 'info')
        return redirect(url_for('main.index'))
    return render_template('new_photo.html', title="New Photo", form=form)