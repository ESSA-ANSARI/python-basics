# Day 6 - BMI Calculator using Functions

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("=== BMI Calculator ===")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
status = interpret_bmi(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"You are classified as: {status}")
