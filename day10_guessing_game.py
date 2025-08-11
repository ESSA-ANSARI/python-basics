# Day 10 - Number Guessing Game 🎯

import random

# 1️⃣ Computer chooses a random number
secret_number = random.randint(1, 50)
attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")

# 2️⃣ Game loop
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1  # Increase attempts count

    if guess < secret_number:
        print("📉 Too low! Try again.")
    elif guess > secret_number:
        print("📈 Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"🏆 You guessed it in {attempts} attempts.")
        break  # Exit the loop
