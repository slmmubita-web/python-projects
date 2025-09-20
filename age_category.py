def get_age():
    while True:
        age_str = input("Enter age: ").strip()
        try:
            age = int(float(age_str))
            if age < 0:
                print("Age cannot be negative. Try again.")
                continue
            return age
        except ValueError:
            print("please enter a valid number (e.g. 21). ")

def category_for_age(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teen"
    elif 20 <= age <= 59:
        return "Adult"
    else:
        return "Senior"

def main():
    name = input("Enter your name: ").strip() or "Anonymous"
    age = get_age()
    category = category_for_age(age)
    print("\nName: {}".format(name))
    print("Age: {}".format(age))
    print("Category: {}".format(category))

if __name__ == "__main__":
    main()
