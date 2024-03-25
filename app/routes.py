from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import User
import sqlalchemy as sa
from flask_login import current_user, login_user, logout_user
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


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.username.data):
            flash("Invalid username or password!")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
