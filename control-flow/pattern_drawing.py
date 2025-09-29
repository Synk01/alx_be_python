# pattern_drawing.py

# --- Input Handling ---
# Prompt User for Pattern Size
size_str = input("Enter the size of the pattern: ")

try:
    size = int(size_str)
except ValueError:
    print("Error: Invalid input. Please enter a whole number.")
    # Exit or handle the error appropriately
    exit()

# Validation for positive integer (from original objective)
if size <= 0:
    print("Error: The size must be a positive integer.")
    exit()

# --- Pattern Drawing ---

# Initialize the row counter for the while loop
row_count = 0

# 1. Use a while loop to iterate through each row of the pattern
while row_count < size:
    
    # 2. Use a for loop to print asterisks for each column
    for col in range(size):
        # Print asterisks side by side without advancing to a new line
        # Using end="" as strictly requested (though end=" " might look better visually)
        print("*", end="") 
    
    # 3. After completing the row, print a newline character
    print()
    
    # Increment the row counter to move to the next row
    row_count += 1
