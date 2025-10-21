# 🎯 Number Guessing Game (Python)

A simple and interactive **command-line number guessing game** built in Python.  
The player tries to guess a secret number between **1 and 100**, with limited attempts depending on the chosen difficulty level.

---

## 🕹️ Gameplay

1. **Choose a difficulty:**
   - 🟢 **Easy** → 9 attempts  
   - 🟡 **Medium** → 6 attempts  
   - 🔴 **Hard** → 3 attempts

2. **Guess the secret number** between 1 and 100.  
   - If your guess is **too low**, the game will say _“Too low!”_  
   - If it’s **too high**, it will say _“Too high!”_  
   - When you find the correct number, it displays your total attempts.

3. If you run out of attempts, the game ends with:
   - Game Over! The secret number was X.

4. After each game, you can choose to **play again** or **exit**:
   - Play again? (Y/N)


---

## ⚙️ Features

✅ Input validation (no crashes on invalid input)  
✅ Three difficulty levels (Easy, Medium, Hard)  
✅ Attempt limit per difficulty  
✅ Dynamic feedback (“Too low”, “Too high”, “Correct”)  
✅ “Play again” loop for continuous play  
✅ Simple and readable code structure  

---

## 🧠 Example Session
Choose difficulty (E/M/H): M
Difficulty: Medium (6 attempts)
Enter your guess (1-100): 50
Too low!
Attempts left: 5
Enter your guess (1-100): 80
Too high!
Attempts left: 4
Enter your guess (1-100): 79
Correct!
You found it in 3 attempts.
Play again? (Y/N): N
Thanks for playing!


🚀 Roadmap / Future Improvements

    📝 Score saving (log attempts and difficulty into a file)

    💬 Hints mode (hot / warm / cold feedback)

    🧱 Refactor into reusable functions (choose_level(), play_round(), main())

    🌍 Localization support (English / Turkish interface)

    🧪 Unit tests for logic validation


🧑‍💻 Author

Tacdin Özmen
Python & Data Science Enthusiast
🇮🇹 Currently based in Como, Italy
📍 GitHub: @tcdn7