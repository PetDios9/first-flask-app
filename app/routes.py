from flask import render_template
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Peter"}
    posts = [
        {
            "author": {"username": "Kevin"},
            "body": "I am learning Flask. It seems pretty easy so far.",
        },
        {
            "author": {"username": "Cindy"},
            "body": "Saw Dune 2 yesterday, such a good movie!",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)
