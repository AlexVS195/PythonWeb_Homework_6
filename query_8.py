# Знайти середній бал, який ставить певний викладач зі своїх предметів.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT teachers.name, ROUND(AVG(grades.grade), 2) AS avg_grade
    FROM teachers
    JOIN subjects ON teachers.id = subjects.teacher_id
    JOIN grades ON subjects.id = grades.subject_id
    GROUP BY teachers.name;
""")

# Отримання результатів
results = cursor.fetchall()

# Виведення результатів
for row in results:
    print(row)

# Закриття підключення
conn.close()