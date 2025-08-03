# day3_logic.py

print("Welcome to Essa's Smart Calculator! 🧠🧮")

while True:
    print("\nOptions: add, subtract, multiply, divide, exit")
    choice = input("Choose operation: ").lower()

    if choice == "exit":
        print("Exiting calculator. Goodbye!")
        break

    if choice in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "add":
            result = num1 + num2
        elif choice == "subtract":
            result = num1 - num2
        elif choice == "multiply":
            result = num1 * num2
        elif choice == "divide":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2

        print(f"Result: {result}")
    else:
        print("Invalid option! Try again.")
