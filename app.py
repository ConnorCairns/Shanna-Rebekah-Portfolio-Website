from flask import Flask, render_template, url_for

app = Flask(__name__)


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





if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

