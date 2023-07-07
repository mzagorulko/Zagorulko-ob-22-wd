import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, GPA INTEGER)")
cursor.execute("INSERT INTO students (name, age, GPA) VALUES (?, ?, ?)", ('John', 20, 4))
cursor.execute("INSERT INTO students (name, age, GPA) VALUES (?, ?, ?)", ('Helen', 21, 5))
cursor.execute("INSERT INTO students (name, age, GPA) VALUES (?, ?, ?)", ('Peter', 19, 3))
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
