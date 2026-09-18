# BMI Category Reporter

**Course:** AIGC 5005 - Artificial Intelligence Capstone Project Preparation  
**Lab:** Lab 01 - Environment and First Repository  
**Prepared by:** Muharrem Kaya

## Project Description

This program calculates a user's Body Mass Index (BMI).

The program asks the user to enter height and weight, validates the entered values, calculates BMI, and reports the BMI category.

## Setup

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

This program does not require any external Python packages.

## Run

Run the program with:

```bash
python bmi.py
```

## Example

```text
BMI Category Reporter
Type 'q' or 'quit' at any time to exit.

Enter your height in cm (100-250): 180
Enter your weight in kg (25-300): 80

Your BMI is 24.7. Category: Normal weight
```

Example with invalid input:

```text
Enter your height in cm (100-250): abc
Invalid input. Please enter a number.

Enter your height in cm (100-250): 300
Height must be between 100 and 250 cm.

Enter your height in cm (100-250): 180
```

## Known Limitations

- The program only uses height and weight to calculate BMI.
- It does not consider age, muscle mass, body composition, or other health factors.
- The height must be between 100 and 250 cm.
- The weight must be between 25 and 300 kg.
- The program is designed for learning purposes only.