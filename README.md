# 🎯 Number Guessing Game (Python)

░█▄█░█▀█░█▀▄░█▀▄░█▀▀░█▀▄░░░█▀▀░█▀█░█▀▄░█▀▀░█▀▄
░█░█░█▀█░█▀▄░█▀▄░█▀▀░█▀▄░░░█░░░█░█░█▀▄░█▀▀░█▀▄
░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀

A fun and interactive **Python command-line game** where you try to guess a secret number between **1 and 100**.  
Challenge yourself with different difficulty levels, track your attempts, and play again as many times as you want! 🚀   

---

## 🕹️ Gameplay

1️⃣ **Choose your difficulty:**
| Level | Attempts | Description |
|--------|-----------|--------------|
| 🟢 Easy   | 9 | For beginners who like to warm up |
| 🟡 Medium | 6 | Balanced challenge |
| 🔴 Hard   | 3 | Only for risk-takers! |

2️⃣ **Start guessing** between 1 and 100  
   - “Too low!” → your number is smaller  
   - “Too high!” → your number is larger  
   - “Correct!” → you found it 🎉 

3️⃣ If you run out of attempts, the game ends with:
   - Game Over! The secret number was X.

4️⃣ After each game, you can choose to **play again** or **exit**:
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

🪪 License

MIT License — free for learning and sharing.