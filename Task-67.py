import sqlite3

conn = sqlite3.connect('database_books.db', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, name TEXT, author TEXT, release DATE)")

cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Мечтают ли андроиды об электроовцах', 'Филип Киндред Дик', '1968-12-12'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Межзвездный скиталец', 'Джек Лондон', '1915-01-01'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Бегущий человек', 'Стивен Кинг.', '1982-01-01'))

cursor.execute("SELECT * FROM books WHERE DATE(release) > '2000-01-01'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
