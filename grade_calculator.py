def calculate_grade(mark):
    """Return a letter grade (A-F) based on the numeric mark."""

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 50:
        return "E"
    else:
        return "F"

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [95, 82, 67, 74, 89]

for name, mark in zip(students, marks):
    grade = calculate_grade(mark)
    print(f"{name}: {mark} - Grade {grade}")
