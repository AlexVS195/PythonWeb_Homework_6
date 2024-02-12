# Знайти середній бал у групах з певного предмета

SELECT groups.name, AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = 'Physics'
GROUP BY groups.name;