# Project Plan (Pseudocode):
# 1. Store weight (kg) and height (m) as variables
# 2. Calculate BMI using formula: BMI=weight/(height**2)
# 3. Determine category based on BMI:
#     BMI < 18.5 → Underweight
#     18.5 <= BMI < 30 → Normal weight
#     BMI >= 30 → Obese
# 4. Output a sentence with BMI value and category

# Store weight and height 
weight = float(input("enter you weight in kg: "))  # get weight in kg
height = float(input("enter you height in meters: "))  # get height in meters

# Calculate BMI
bmi=weight/(height**2)

# Determine category
if bmi<18.5:
    category = "underweight"
elif 18.5<= bmi<30:
    category = "normal weight"
else:
    category = "obese"

# print the result
print ("Your BMI is " + str(bmi) + ", which classifies you as "+ category + ".")
