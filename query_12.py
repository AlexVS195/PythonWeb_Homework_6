# Оцінки студентів у певній групі з певного предмета на останньому занятті.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT students.name, grades.grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE students.group_id = 1 AND subjects.name = 'Mathematics'
    AND grades.date = (
        SELECT MAX(date)
        FROM grades
        WHERE grades.student_id = students.id
        AND grades.subject_id = subjects.id
    );
""")

# Отримання результатів
results = cursor.fetchall()

# Виведення результатів
for row in results:
    print(row)

# Закриття підключення
conn.close()