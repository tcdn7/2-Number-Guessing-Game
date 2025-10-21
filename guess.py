import random

level = input("Choose difficulty (E/M/H): ").strip().upper()
while level not in ['E', 'M', 'H']:
    print("Invalid difficulty level. Please choose E, M, or H.")
    level= input("Choose difficulty (E/M/H): ").strip().upper()

if level == 'E': 
    max_attempts = 9
elif level == 'M': 
    max_attempts = 6        
else: 
    max_attempts = 3
level_name = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}[level]    
print(f"Difficulty: {level_name} ({max_attempts} attempts)")    

secret=random.randint(1, 100)
attempts=0

while attempts < max_attempts:
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
        if attempts < max_attempts:
            print(f"Attempts left: {max_attempts - attempts}")
    elif guess > secret:
        print("Too high!")
        if attempts < max_attempts:
            print(f"Attempts left: {max_attempts - attempts}")
    else:
        print("Correct!")
        print(f"You found it in {attempts} attempts.")
        break
else:
    print(f"Game Over! The secret number was {secret}.")
