# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


BMI = round(weight/ (height ** 2), 2)
if (BMI < 18.5):
    print(f"your BMI is {BMI}, is underweight")
elif (BMI < 25):
    print(f"your BMI is {BMI}, is normal weight")
elif (BMI < 30):
    print(f"your BMI is {BMI}, is slightly overweight")
elif (BMI < 35):
    print(f"your BMI is {BMI}, is obese")
else:
    print(f"your BMI is {BMI}, is clinically obese")
