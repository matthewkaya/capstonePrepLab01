print("BMI Category Reporter")

try:
    height_cm = float(input("Enter your height in cm (100-250): "))
    weight_kg = float(input("Enter your weight in kg (25-300): "))

    if height_cm < 100 or height_cm > 250:
        print("Height must be between 100 and 250 cm.")
    elif weight_kg < 25 or weight_kg > 300:
        print("Weight must be between 25 and 300 kg.")
    else:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        print(f"Your BMI is {bmi:.1f}. Category: {category}")

except ValueError:
    print("Invalid input. Please enter numbers only.")