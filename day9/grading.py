student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}

for person in student_scores:
    score = student_scores[person]
    grade = "fail"
    if score > 90 and score <= 100:
        grade = "Outstanding"
    elif score > 80 and score <= 90:
        grade = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        grade = "Acceptable"
    student_grades[person] = grade

print(student_grades)
