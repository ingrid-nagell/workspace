from flask import Flask, render_template

from post import Post

app = Flask(__name__)

blog = Post()

@app.route('/')
def home():
    posts = blog.response
    return render_template("index.html", blog_posts = posts)

@app.route('/post/<id>')
def get_post(id):
    id_as_int = int(id)
    no_of_posts = blog.no_of_posts


    post = blog.get_post(id_as_int)
    title = post["title"]
    subtitle = post["subtitle"]
    body = post["body"]

    return render_template(
        "post.html",
        post_id = id_as_int,
        post_title = title,
        post_subtitle = subtitle,
        post_body = body,
        no_of_posts = no_of_posts,
    )

if __name__ == "__main__":
    app.run(debug=True)
