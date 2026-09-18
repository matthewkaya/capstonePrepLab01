print("BMI Category Reporter Lab01")
print("Author Muharrem Kaya")

print("Type 'q' or 'quit' at any time to exit.")

# Height input loop

while True:
    height_input = input("Enter your height in cm (100-250): ")
    if height_input.lower() == "q" or height_input.lower() == "quit":
        print("Program ended.")
        quit()

    try:
        height_cm = float(height_input)
        if height_cm < 100 or height_cm > 250:
            print("Height must be between 100 and 250 cm.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a number.")

# Weight input loop

while True:
    weight_input = input("Enter your weight in kg (25-300): ")
    if weight_input.lower() == "q" or weight_input.lower() == "quit":
        print("Program ended.")
        quit()

    try:
        weight_kg = float(weight_input)
        if weight_kg < 25 or weight_kg > 300:
            print("Weight must be between 25 and 300 kg.")

        else:
            break

    except ValueError:
        print("Invalid input. Please enter a number.")

# BMI calculation

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
# BMI category

if bmi < 18.5:
    category = "Underweight"

elif bmi < 25:
    category = "Normal weight"

elif bmi < 30:
    category = "Overweight"

else:
    category = "Obesity"

# Result

print(f"Your BMI is {bmi:.1f}. Category: {category}")