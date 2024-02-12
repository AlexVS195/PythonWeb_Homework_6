# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT students.id, students.name, AVG(grades.grade) AS avg_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    GROUP BY students.id, students.name
    ORDER BY avg_grade DESC
    LIMIT 5;
""")

# Отримання результатів
results = cursor.fetchall()

# Виведення результатів
for row in results:
    print(row)

# Закриття підключення
conn.close()