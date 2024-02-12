# Знайти список студентів у певній групі.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT name
    FROM students
    WHERE group_id = 1;
""")

# Отримання результатів
results = cursor.fetchall()

# Виведення результатів
for row in results:
    print(row)

# Закриття підключення
conn.close()