Height = float(input("Enter your height (in metres): "))
Weight = float(input("Enter your weight (in kilograms): "))
BMI = Weight / (Height ** 2)
if BMI >= 30:
    print("Obesity")
elif 25 < BMI <= 29:
    print("Overweight")
elif 18.5 < BMI <= 25:
    print("Normal")
elif BMI < 18.5:
    print("Underweight")
else:
    print("There was an issue due to invalid height or weight")