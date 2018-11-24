from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.main.forms import contact_form
from app.main.utils import send_email, get_page_images
from app import db
from app.models import PageImages, Pages, User
from app.main.forms import Add_Photoshoot_Photo, New_photoshoot
from app.pictures.utils import s3_upload, save_pic, del_pic
from app.users.utils import get_photo, last_login
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        last_login(current_user)
    return render_template('index.html')


@main.route('/about/')
def about():
    return render_template('about.html')

@main.route('/new_photoshoot/', methods=['GET','POST'])
@login_required
@User.must_be_role("Admin")
def new_photoshoot():
    form = New_photoshoot()
    if form.validate_on_submit():
        photoshoot = Pages(page_name=(form.name.data).lower(), page_category=form.category.data, page_text=form.text.data)
        db.session.add(photoshoot)
        db.session.commit()
        flash('Photoshoot added, please now add an image', 'info')
        return redirect(url_for('main.new_picture'))
    return render_template('new_photoshoot.html', form=form)

@main.route('/new_photoshoot/picture/', methods=['GET','POST'])
@login_required
@User.must_be_role("Admin")
def new_picture():
    form = Add_Photoshoot_Photo()
    if form.validate_on_submit():
        page = Pages.query.filter_by(page_name=str(form.page.data).lower()).first()
        photo = PageImages(photo_name=(form.name.data).lower(), page=page)
        db.session.add(photo)
        db.session.commit()
        save_pic(form.picture.data, form.name.data)
        s3_upload(form.name.data)
        del_pic(form.name.data)
        flash('Image information added', 'info')
        return redirect(url_for('main.new_picture'))
    return render_template('new_picture.html', form=form)


@main.route('/contact/', methods=['GET','POST'])
def contact():
    form = contact_form()
    if form.validate_on_submit():
        send_email(form)
        flash(f'Email sent!', 'success')
        return redirect(url_for('main.index'))
    return render_template('contact.html', form=form)

@main.route('/category/<page>')
def category(page):
    pages = Pages.query.filter_by(page_category=page).all()
    images_array = []
    get_page_images(pages, images_array)
    return render_template('photoshoots/category.html', pages=pages, images_array=images_array, page=page)

@main.route('/photoshoot/<photoshoot>')
def portraits_photoshoot(photoshoot):
    page = Pages.query.filter_by(page_name=photoshoot).first_or_404()
    photo = PageImages.query.filter_by(page_id=page.id).all()
    photo_list = []
    get_photo(photo, photo_list)
    return render_template('photoshoots/photoshoot.html', page=page, photo=photo_list, enumerate=enumerate)