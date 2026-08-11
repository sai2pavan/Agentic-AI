height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")