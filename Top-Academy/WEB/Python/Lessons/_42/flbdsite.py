from flask import Flask, render_template, url_for, request, flash, session, redirect, g
import os
import sqlite3

from FDataBase import FDataBase

DATABASE = 'flsk.db'
DEBUG = True
SECRET_KEY = 'd0796806ca09b2d12eb11478fa352d7a97db48cb098714'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu(),
                           posts=dbase.get_post_announcement())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post_text']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post_text'], request.form['url'])
            if not res:
                flash("Error with adding post", category='error')
            else:
                flash("Post added successfully", category='success')
        else:
            flash("Error with adding data (short length)", category='error')
    return render_template('add_post.html', menu=dbase.get_menu(), title='Add Post')


@app.route("/post/<alias>")
def show_post(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(alias)

    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Page Not Found", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
