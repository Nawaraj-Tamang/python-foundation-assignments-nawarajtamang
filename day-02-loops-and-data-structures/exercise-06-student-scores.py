"""
Exercise: Student Score Dictionary
Student: Nawaraj Tamang
Day: 2
"""

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Print every student and score
for name, score in student_scores.items():
    print(f"{name}: {score}")

# 2. Only students who scored at least 60 (dictionary comprehension)
passing_students = {name: score for name, score in student_scores.items() if score >= 60}

# 3. Student with the highest score
top_student = max(student_scores, key=student_scores.get)

# 4. Average score
average_score = sum(student_scores.values()) / len(student_scores)

# Output
print(f"\nPassing students (>= 60): {passing_students}")
print(f"Top student: {top_student} ({student_scores[top_student]})")
print(f"Average score: {average_score:.2f}")