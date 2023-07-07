import sqlite3

conn = sqlite3.connect('database_movies.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating REAL)")

cursor.execute("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)", ('Оно', 'Ужасы', 8.9))
cursor.execute("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)", ('Индиана Джонс', 'Приключения', 8.1))
cursor.execute("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)", ('Джуманджи', 'Фантастика', 7.9))

cursor.execute("SELECT * FROM movies WHERE genre = 'Фантастика'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
