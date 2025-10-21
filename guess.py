import random

secret=random.randint(1, 100)
attempts=0

while True:
    try:
        guess=int(input("Enter your guess (1-100): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts+=1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        print(f"You found it in {attempts} attempts.")
        break

# print(secret)  # For testing only
