# day2_basics.py

# Let's start with variables
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f"Nice to meet you, {name}! You're {age} years old.")

# Let's do some math!
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# Add, subtract, multiply, divide
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2

print("\n--- Results ---")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div:.2f}")
print(f"{num1} % {num2} = {mod}")