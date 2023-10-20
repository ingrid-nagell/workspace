from time import process_time
from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)

@app.route("/")
def home():
    year = datetime.now().year
    return render_template("index.html", year=year)

@app.route("/guess/<name>")
def guess(name):
    year = datetime.now().year
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("guess_the_name.html", year=year, name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", all_posts = posts)


if __name__ == "__main__":
    app.run(debug=True)