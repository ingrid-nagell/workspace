from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    this_year = datetime.now().year
    return render_template("index.html", this_year=this_year)


if __name__ == "__main__":
    app.run(debug=True)