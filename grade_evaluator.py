name = input("Enter your student name: ")
score = float(input("Enter (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

print(f"\nStudent: {name}")
print(f"Score: {score}")
print(f"Grade: {grade}")
