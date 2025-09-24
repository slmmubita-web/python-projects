names = ["Mubita", "Muyunda", "Rose", "Rosemary", "Sikwibele", "Sylvia"]
marks = [85, 94, 87, 74, 97]
average = sum(marks) / len(marks)

def grade(m):
    if m >= 90:
        return "A"
    elif m >= 80:
        return "B"
    elif m >= 70:
        return "C"
    elif m >= 60:
        return "D"
    else:
        return "F"

for i in range(len(names)):
    print(f"{names[i]}: {marks[i]} - Grade {grade(marks[i])}")
print(f"Average marks: {average:. 1f}")
