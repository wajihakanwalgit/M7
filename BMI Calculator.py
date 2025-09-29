
height_cm = float(input("Enter your height in centimeters: "))
weight_kg = float(input("Enter your weight in kilograms: "))


bmi = weight_kg / (height_cm / 100) ** 2


print(f"\nYour BMI is: {bmi:.2f}")


if bmi <= 18.4:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Healthy")
elif bmi <= 29.9:
    print("Category: Overweight")
elif bmi <= 34.9:
    print("Category: Severely Overweight")
elif bmi <= 39.9:
    print("Category: Obese")
else:
    print("Category: Severely Obese")
