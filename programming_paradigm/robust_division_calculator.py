# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
 # to convert inputs to float and set exceptions
        numerator = float(numerator)
        denominator = float(denominator)
        try:
            result = numerator / denominator
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
