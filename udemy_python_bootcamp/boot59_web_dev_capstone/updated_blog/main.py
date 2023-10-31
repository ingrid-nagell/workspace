from flask import Flask, render_template
from blog_content import GetBlogPosts

app = Flask(__name__)

@app.route('/')
def home():
    all_content = posts.content
    return render_template("index.html", all_content=all_content)

@app.route('/post/<id>')
def post(id):
    article = posts.get_single_post(int(id))
    return render_template("post.html", article=article, id=id)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    posts = GetBlogPosts()
    app.run(debug=True)