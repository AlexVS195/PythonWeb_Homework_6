# Середній бал, який певний викладач ставить певному студентові.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT AVG(grades.grade) AS avg_grade
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE teachers.name = 'Paul Ramos' AND grades.student_id = 1;
""")

# Отримання результату
result = cursor.fetchone()

# Виведення результату
print(result[0] if result else "No data")

# Закриття підключення
conn.close()