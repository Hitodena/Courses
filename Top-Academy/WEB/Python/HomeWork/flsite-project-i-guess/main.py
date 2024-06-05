from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd0796806ca09b2d12eb11478fa352d7a97db48cb098714'

menu = [
    {'name': 'Home', 'url': 'home'},
    {'name': 'About Us', 'url': 'about'}
]


@app.route('/')
@app.route('/home')
def home():
    print(url_for("home"))
    return render_template('base.html', title='Home', menu=menu)


@app.route('/about')
def about():
    print(url_for("about"))
    return render_template('base.html', title='About Us', menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
