height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# BMI Calculation
BMI = weight / (height / 100)**2
print(f"Your BMI is: {BMI:.2f}")

# BMI Classification
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are moderately obese.")
elif BMI <= 39.9:
    print("You are severely obese.")
else:
    print("You are very severely obese.")

   