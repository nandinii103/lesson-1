height = float(input("Please enter your height in centimetres:"))
weight = float(input("Please enter your weight in kilograms: "))

height = height/100
bmi = weight / (height * height)

print("your BMI is:",bmi)
if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You are normal weight")
elif bmi <= 65:
    print("You are overweight")
else:
    print("You are obese")
    


