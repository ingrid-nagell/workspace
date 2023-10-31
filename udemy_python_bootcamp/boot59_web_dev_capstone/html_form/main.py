from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form['name']
        pwd = request.form['pwd']
        return render_template("login.html", username = name, password = pwd)

if __name__ == "__main__":
    app.run(debug=True)