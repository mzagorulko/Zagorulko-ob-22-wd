import sqlite3

conn = sqlite3.connect('database_employees.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, function TEXT, salary REAL)")

cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Старк Тони Викторович', 'Миллиардер', 1999999))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Халк Брюс Беннерович', 'Вышибала', 250000))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Паркер Питер Игоревич', 'Стажер', 3000))

cursor.execute("SELECT * FROM employees WHERE function = 'Стажер'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
