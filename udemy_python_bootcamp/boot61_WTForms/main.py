from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap4
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from loguru import logger

WTF_CSRF_SECRET_KEY = 'qwe123'
VERIFIED_USERS = {"admin@email.com":  "12345678"}


def validate_credentials(email, pwd):
    if email in VERIFIED_USERS:
        if VERIFIED_USERS[email] == pwd:
            logger.info("Successful log in attempt.")
            return True
    else:
        logger.info("Invalid log in attempt.")
        return False

class LoginForm(FlaskForm):
    email = StringField(label="Email:", validators=[Email()])
    password = PasswordField(label="Password:", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = WTF_CSRF_SECRET_KEY
bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'] )
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if validate_credentials(email=login_form.email.data, pwd=login_form.password.data):
            return render_template('success.html')
        else:
            return render_template("denied.html")
    else:
        logger.warning(f"Unsuccesful login attempt with {login_form.email.data}.")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)