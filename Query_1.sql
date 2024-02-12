# Знайти 5 студентів із найбільшим середнім балом з усіх предметів:

SELECT students.name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 5;