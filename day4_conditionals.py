# Day 4 - Grade Evaluator

print("Welcome to the Grade Evaluator 🎓")

# Input
name = input("Enter your name: ")
marks = []

for i in range(1, 6):
    score = float(input(f"Enter marks for subject {i} (out of 100): "))
    marks.append(score)

# Processing
total = sum(marks)
percentage = (total / 500) * 100

# Output - Conditional logic
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'

print(f"\nHello, {name}! Your total is {total}/500")
print(f"Your percentage: {percentage:.2f}%")
print(f"Your Grade: {grade}")
