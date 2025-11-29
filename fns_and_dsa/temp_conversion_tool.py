
#PART 1
# At the top of your script, define two global variables FAHRENHEIT_TO_CELSIUS_FACTOR and 
#CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).

# PART 1: Conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# PART 2: Conversion functions using global
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # explicitly declare global
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # explicitly declare global
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# PART 3: User input
user_prompt = float(input("Enter the temperature to convert: "))

# Restrict input to only C or F
while True:
    unit = input("Enter either C or F: ").upper()
    if unit in ["C", "F"]:
        break
    print("Invalid input. Please enter only 'C' or 'F'.")

# PART 4: Perform conversion
if unit == "C":
    result = convert_to_fahrenheit(user_prompt)
    print(f"{user_prompt}°C is {result}°F")
else:  # unit == "F"
    result = convert_to_celsius(user_prompt)
    print(f"{user_prompt}°F is {result}°C")
