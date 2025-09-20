def calculate(a, b, op):
   try:
    if op == "+":
        return a + b
    if op == "_":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    if op == "%":
        return a % b
    if op == "**":
        return a ** b
    raise ValueError("Unsupported oprator")
   except ZeroDivisionError:
    return "Error: division by zero"

def main():
   try:
    a = float(input("Enter the first number: "))
   except ValueError:
    print("Invalid number for first value.")
    return
   op = input("Enter an operator (+, _, *, /, %, **: ").string()
   try:
    b = float(input("Enter the second number: "))
   except ValueError:
    print("Invalid number for second value.")
    return
if __name__ == " __main__":
    main()

