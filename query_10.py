# Список курсів, які певному студенту читає певний викладач.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT subjects.name
    FROM subjects
    JOIN grades ON subjects.id = grades.subject_id
    JOIN students ON grades.student_id = students.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE students.name = 'Erica Fernandez' AND teachers.name = 'John Anderson';
""")

# Отримання результатів
results = cursor.fetchall()

# Виведення результатів
for row in results:
    print(row)

# Закриття підключення
conn.close()