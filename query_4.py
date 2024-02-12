# Знайти середній бал на потоці (по всій таблиці оцінок).

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT AVG(grade) AS avg_grade
    FROM grades;
""")

# Отримання результатів
result = cursor.fetchone()

# Виведення результату
print(result)

# Закриття підключення
conn.close()