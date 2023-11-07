from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = '1234'

@app.route("/")
def index():
    flash("Registrer tilbud:")
    return render_template("login.html")

@app.route("/registre_tilbud", methods=['POST'])
def registrering():
    flash("Ditt brukernavn: " + str(request.form['user_input']))
    request.form['user_input']
    return render_template("registrering.html")

if __name__ == "__main__":
    app.run(debug=True)