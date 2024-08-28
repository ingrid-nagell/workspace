from sqlite3 import IntegrityError
from time import strftime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

db = SQLAlchemy()
ckeditor = CKEditor()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    Bootstrap5(app)

    # CONNECT TO DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
    db.init_app(app)

    ckeditor.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app

app = create_app()


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class NewBlogPostForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle")
    author = StringField(label="Author")
    img_url = StringField(label="Image url")
    body = CKEditorField(label="Content")
    submit = SubmitField(label="Submit new post")


@app.route('/')
def get_all_posts():
    posts_query = db.session.execute(db.select(BlogPost).order_by(BlogPost.id.desc()))
    posts = posts_query.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/blog')
def show_post():
    post_id = request.args.get("post_id") 
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def create_post():
    form = NewBlogPostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title = request.form.get('title'),
            subtitle = request.form.get('subtitle'),
            date = datetime.today().strftime("%B %d, %Y"),
            body = request.form.get('body'),
            author = request.form.get('author'),
            img_url = request.form.get('img_url'),
        )
        try:
            db.session.add(new_post)
            db.session.commit()
        except IntegrityError:
            #PRINT ERROR
            return redirect(url_for("get_all_posts"))
        finally:
            return redirect(url_for("get_all_posts"))
 
    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    print("-------------",post_id, "------------")
    post = db.get_or_404(BlogPost, post_id)
    edit_form = NewBlogPostForm(
        title = post.title,
        subtitle = post.subtitle,
        author = post.author,
        img_url = post.img_url,
        body = post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data    
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form = edit_form)


@app.route('/delete-post')
def delete_post():
    post_id = request.args.get("post_id") 
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
