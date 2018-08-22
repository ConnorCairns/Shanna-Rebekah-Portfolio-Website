from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ihatecoursework'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/double-exposure/')
def double_exposure():
    x = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
    return render_template('double-exposure.html', x=x, enumerate=enumerate)

@app.route('/register', methods=['GET','POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

