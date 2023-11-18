import sqlite3

PATH = "C:\\Users\\G020772\\repos\\workspace\\udemy_python_bootcamp\\boot63_advanced_databases\\instance\\new-books-collection.db"
# PATH = "C:\\Users\\G020772\\repos\\workspace\\udemy_python_bootcamp\\boot63_advanced_databases\\books-collection.db"

db = sqlite3.connect(PATH)

cursor = db.cursor()

result = cursor.execute("SELECT * FROM books")

print(result.fetchall())