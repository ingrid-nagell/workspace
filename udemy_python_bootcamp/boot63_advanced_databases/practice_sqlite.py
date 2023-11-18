import sqlite3

PATH = "udemy_python_bootcamp\\boot63_advanced_databases\\books-collection.db"
db = sqlite3.connect(PATH)

cursor = db.cursor()

cursor.execute(
    """
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title varchar(250) NOT NULL UNIQUE,
        author varchar(250) NOT NULL,
        rating FLOAT NOT NULL
        )
    """
    )

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")

db.commit()