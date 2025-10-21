import random

secret=random.randint(1, 100)
guess=int(input("Enter your guess (1-100): "))

if guess < secret:
    print("Too low!")
elif guess > secret:
    print("Too high!")
else:
    print("Correct!")

# print(secret)  # For testing only
