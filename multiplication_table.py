num = int(input("Enter a number to print its multiplication table: "))
print(f"\nMultiplication Table for {num}.")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\nMultiplication Tables for numbers 1 to 5:")
for n in range(1, 6):
    print(f"\nTable for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
