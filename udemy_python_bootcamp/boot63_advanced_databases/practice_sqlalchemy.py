from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

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

if __name__ == "__main__":
    # Create a db:

    # with app.app_context():
    #     db.create_all()


    # Add more records:

    # with app.app_context():
    #     new_book = Book(id=2, title="Harry Potter 2", author="J. K. Rowling", rating=9.8)
    #     db.session.add(new_book)
    #     db.session.commit()


    # Get records:
    # with app.app_context():
    #     result = db.session.execute(db.select(Book).order_by(Book.title))
    #     all_books = result.scalars()
    #     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    #     print(all_books.fetchall())

    # with app.app_context():
    #     # book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    #     # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    #     # db.session.commit() 
    #     print(Book.query.all())

    # Delete record by id:
    book_id = 2
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()