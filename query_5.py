# Знайти які курси читає певний викладач.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT subjects.name
    FROM subjects
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE teachers.name = 'Christopher Ware';
""")

# Отримання результатів
results = cursor.fetchall()

# Виведення результатів
for row in results:
    print(row)

# Закриття підключення
conn.close()