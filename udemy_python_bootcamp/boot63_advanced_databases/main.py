from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-library.db"

db = SQLAlchemy()

db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys will be auto-updated when adding more records.
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


def query_books():
    with app.app_context():
        return Book.query.all()

def query_book_from_id(id):
    with app.app_context():
        # return db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        return Book.query.get(id)

def update_book_rating_from_id(id, new_rating):
    with app.app_context():
        book_to_update = Book.query.get(id)
        book_to_update.rating = new_rating
        db.session.commit()

def add_book(title, author, rating):
    with app.app_context():
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

def delete_book_from_id(id):
    with app.app_context():
        book_to_delete = db.get_or_404(Book, id)
        db.session.delete(book_to_delete)
        db.session.commit()


# Routes content:
@app.route('/')
def home():
    all_books = query_books()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        add_book(title, author, rating)

        return redirect(url_for('home'))

    return render_template("add.html")


@app.route('/edit', methods=["GET", "POST"])
def edit_rating():
    id = request.args.get('id')
    book = query_book_from_id(id)

    if request.method == "POST":
        update_book_rating_from_id(id, request.form["new_rating"])

        return redirect(url_for('home'))

    return render_template("edit_rating.html", id=id, book=book)


@app.route('/delete')
def delete():
    id = request.args.get('id')
    print("---------> ", query_book_from_id(id))
    delete_book_from_id(id)
    
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
