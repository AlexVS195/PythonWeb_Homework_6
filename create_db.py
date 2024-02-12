import sqlite3
from faker import Faker
import random

# Створення бази даних та підключення до неї
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''CREATE TABLE students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER
                )''')

cursor.execute('''CREATE TABLE groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER
                )''')

cursor.execute('''CREATE TABLE grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT
                )''')

# Вставка даних у таблицю groups
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))
group_ids = list(range(1, len(groups) + 1))

# Вставка даних у таблицю teachers
fake = Faker()
teachers = [fake.name() for _ in range(3)]
for teacher in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher,))
teacher_ids = list(range(1, len(teachers) + 1))

# Вставка даних у таблицю subjects
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']
for subject, teacher_id in zip(subjects, teacher_ids):
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))
subject_ids = list(range(1, len(subjects) + 1))

# Вставка даних у таблицю students та grades
for _ in range(30):
    name = fake.name()
    group_id = random.choice(group_ids)
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
    student_id = cursor.lastrowid
    for subject_id in subject_ids:
        grade = random.randint(60, 100)
        date = fake.date_between(start_date='-1y', end_date='today')
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date))

# Збереження змін у базі даних
conn.commit()
conn.close()