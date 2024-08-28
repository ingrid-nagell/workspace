from datetime import date
from msilib.schema import Error
from sqlite3 import IntegrityError
from flask import Flask, abort, render_template, redirect, url_for, flash, request, session
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentsForm


ckeditor = CKEditor()

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8BYkEfBA6OBXox7fasfC0sKR6bzcxv'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_project.db'
    login_manager.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    return app

app = create_app()
Bootstrap5(app)

# CONFIGURE TABLES
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int]         = mapped_column(Integer, primary_key=True)
    username: Mapped[str]   = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str]      = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str]   = mapped_column(String(250), nullable=False)


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int]         = mapped_column(Integer, primary_key=True)
    title: Mapped[str]      = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str]   = mapped_column(String(250), nullable=False)
    date: Mapped[str]       = mapped_column(String(250), nullable=False)
    body: Mapped[str]       = mapped_column(Text, nullable=False)
    author: Mapped[str]     = mapped_column(String(250), nullable=False)
    author_id: Mapped[int]  = mapped_column(Integer, db.ForeignKey("users.id"))
    img_url: Mapped[str]    = mapped_column(String(250), nullable=False)

class Comments(db.Model):
    __tablename__ = "comments"
    id: Mapped[int]         = mapped_column(Integer, primary_key=True)
    date: Mapped[str]       = mapped_column(String(250), nullable=False)
    body: Mapped[str]       = mapped_column(Text, nullable=False)
    author: Mapped[str]     = mapped_column(String(250), nullable=False)
    author_id: Mapped[int]  = mapped_column(Integer, db.ForeignKey("users.id"))
    post_id: Mapped[int]    = mapped_column(Integer)


@login_manager.user_loader
def load_user(id):
    return db.get_or_404(User, id)

with app.app_context():
    db.create_all()


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('get_all_posts'))

    form = RegisterForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        # Check if username exists
        username = form.username.data
        username_exists = db.session.execute(db.select(User).where(User.username == username)).scalar()
        
        email = form.email.data
        email_exists = db.session.execute(db.select(User).where(User.email == email)).scalar()
        
        if username_exists or email_exists:
            if username_exists:
                flash(f'Username "{username}" is already registered.')
            if email_exists:
                flash(f'Email "{email}" is already registered.')
            flash(f'Go to the log in page to log in.')
            return redirect(url_for('register'))

        pwhash = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            username=username,
            email=email,
            password=pwhash,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            flash("An error occured. Please try again.")
            return redirect(url_for('register'))
        else:
            login_user(new_user)
            flash(f"Your account was successfully registered with username: {current_user.username}.")
            return redirect(url_for('get_all_posts'))
    return render_template('register.html', form=form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.args.get("username")
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            input_password = form.password.data
            if check_password_hash(pwhash=user.password, password=input_password):
                # Log in user with Flask Log In
                login_user(user)
                username = current_user.username
                flash(f"You are logged in as {username}")
                return redirect(url_for('get_all_posts'))
            else:
                flash("Password is incorrect, please try again.")
        else:
            flash("No such email in the database. Go to the register-page to open an account.")
    # Add username as default in form if coming from registerpage
    return render_template('login.html', username=username, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template('index.html', all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    blog_id = post_id
    requested_post = db.get_or_404(BlogPost, blog_id)
    comments = db.get_or_404(db.select(Comments).where(Comments.post_id == blog_id)).scalars()

    form = CommentsForm()
    if form.validate_on_submit():

        if current_user.is_authenticated:
            author = current_user.username
            author_id = current_user.id
        else:
            author = "Guest"
            author_id = 9999

        new_comment = Comments(
            date = date.today().strftime("%B %d, %Y"),
            body = form.body.data,
            author = author,
            author_id = author_id,
            post_id = blog_id,
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template('post.html', post=requested_post, form=form, comments=comments)


@app.route("/new-post", methods=["GET", "POST"])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.username,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        author_id=post.author_id,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user.username
        post.author_id = current_user.id
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))
    return render_template('make-post.html', form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)
