"""
Day 12: Guess-the-Number Game Generates a random number between 1 and 50.
The user keeps guessing untill they find the correct number.
Hints "Too high" / "Too low" are given.
The total number of attempts is diplayed at the end.
"""

import random
def main():
    number_to_guess = randon.randint(1, 50)

    print("I'm thinking of a number between 1 and 50... can you guess it?")
    while True:
    guess_str = input("Enter your guess: ").strip()

    if not guess_str:
        print("Please enter a number.")
        continue

    if guess_str.lower() in ("q", "quit", "exist"):
        print(f"You gave up.The number was {number, _to_guess}. ")
        break

    try:
        guess = int(guess_str)
    except ValueError:
        print("That's not a valid integer. Try again. ")
        continue

    if guess < 1 or guess > 50:
        print("You guess must be between 1 and 50. ")
        continue
    attempts += 1
    if guess < number < number_to_guess:
        print("Too low. ")
    elif guess > number_to_guess:
        print("Too high. ")
    else:
        print(f" corroct! The number was {number, _to_guess}. ")

        print(f"You found it in {attempts} attempt{'s' if attempts != 1 else''}.")
        break

if __name__ =="__main__":
    main()
