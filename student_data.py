def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

students = [
    {"name": "Alice", "age": 20, "marks": 95},
    {"name": "Bob", "age": 21, "marks": 82},
    {"name": "Charlie", "age": 19, "marks": 67},
    {"name": "David", "age": 22, "marks": 74},
    {"name": "Eve", "age": 20, "marks": 58},
]

for student in students:
    student["grade"] = calculate_grade(student["marks"])

for student in students:
    print(f"{student['name']}: Age {student['age']},marks {student['marks']} - Grade: {student['grade']}")
