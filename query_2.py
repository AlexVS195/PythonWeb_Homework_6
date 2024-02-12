# Знайти студента із найвищим середнім балом з певного предмета.

import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання SQL-запиту
cursor.execute("""
    SELECT students.id, students.name, AVG(grades.grade) AS avg_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.name = 'Mathematics'
    GROUP BY students.id, students.name
    ORDER BY avg_grade DESC
    LIMIT 1;
""")

# Отримання результатів
result = cursor.fetchone()

# Виведення результату
print(result)

# Закриття підключення
conn.close()