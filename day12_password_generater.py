import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔑 Welcome to the Python Password Generator!")
while True:
    try:
        length = int(input("Enter password length (min 6): "))
        if length < 6:
            print("⚠️ Password too short! Please enter at least 6.")
            continue
        password = generate_password(length)
        print(f"✅ Your generated password: {password}\n")
    except ValueError:
        print("❌ Please enter a valid number.")

    again = input("🔄 Generate another password? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Thanks for using the Password Generator!")
        break
