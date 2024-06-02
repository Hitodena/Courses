from flask import Flask, render_template, url_for

app = Flask(__name__)


menu = [
    {'name': 'Main page', 'url': 'index'},
    {'name': 'About us', 'url': 'about'},
    {'name': 'Backfeed', 'url': 'contact'}
]


@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template('index.html', title="Index", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='About us', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"User: {username}"


if __name__ == "__main__":
    app.run(debug=True)
