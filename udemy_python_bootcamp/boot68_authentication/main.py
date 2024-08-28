from sqlite3 import IntegrityError
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# clients:
login_manager = LoginManager()
db = SQLAlchemy()

# initiate app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    # CONNECT TO DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    db.init_app(app)

    login_manager.init_app(app)

    return app

app = create_app()

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(id):
    return db.get_or_404(User, id)


# routes
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register',  methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if result:
            flash("Email is already registered.")
            return redirect(url_for('register'))

        pwhash = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=pwhash
        )
        

        try:
            db.session.add(new_user)
        except Exception as e:
            flash(f"Error: {e}")
            return redirect(url_for("register.html"))
        else:
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        print(email, password)    
        try:
            requested_user = db.session.execute(db.select(User).where(User.email==email)).scalar()
            if requested_user == None:
                flash("Invalid username")
                return redirect(url_for("login"))
        except Exception as e:
            flash(f"Error: {e}")
        else:
            if check_password_hash(pwhash=requested_user.password, password=password):
                login_user(requested_user)
                return redirect(url_for("secrets"))
            else:
                flash("Invalid password")            

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
