import random

secret=random.randint(1, 100)
attempts=0

while True:
    guess=int(input("Enter your guess (1-100): "))
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
