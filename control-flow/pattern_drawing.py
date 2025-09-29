while True:
    try:  
        size_str = input("Enter a positive integer for the square size (n): ")
        size = int(size_str)

        # To check if the integer is positive
        if size > 0:
            break
        else:
            print("Error: The size must be a positive integer greater than zero.")
            
    except ValueError:
        # Catch errors if the input cannot be converted to an integer
        print("Error: Invalid input. Please enter a whole number.")

print(f"\nDrawing a {size}x{size} square pattern:")

for row in range(size):
    for col in range(size):
        print("*", end=" ")

    print()
