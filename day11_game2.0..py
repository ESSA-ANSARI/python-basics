import random
from re import T
from sre_constants import SRE_INFO_CHARSET

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty: EASY, MEDIUM, HARD")
  
    difficulty = input("Enter Diffculty: ").lower()

    if difficulty == "easy":
        max_num = 50
        max_attempts = 10
        print("You have 10 attempts to guess the number between 1 and 50.")

    elif difficulty == "medium":
        max_num = 100
        max_attempts = 7
        print("You have 7 attempts to guess the number between 1 to 100.")

    elif difficulty == "hard":
        max_num = 200
        max_attempts = 5
        print("You have 5  attempts to guess the number between 1 to 200.")
        print("Good luck!")

    else:
        print("Invalid choice, Defaulting to medium.")
        max_num = 100
        max_attempts = 7

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"Guess the number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while True:
       guess = int(input("Enter your Guess: "))
       attempts += 1

       if guess < secret_number:
            print("Too low, try again.")
       elif guess > secret_number:
            print("too High, try again.")
       else:
           print(f"Correct! The number was {secret_number}.")
           print(f"you guessed it in {attempts} attempts.")
           break

       if attempts >= max_attempts:
            print(f" Game over! The number was {secret_number}.")
            break
         
while True:
    play_game()
    again = input("Do you want to play again? (yes/ No).").lower()
    if again != "yes":
        print("Thanks for playing!")
        break

   


