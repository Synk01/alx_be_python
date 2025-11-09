#num1 = int(input("Enter the first number: "))  # Convert input to integer
#num2 = int(input("Enter the second number: "))

# Perform the addition and store the result
#sum = num1 + num2

#print("The sum of", num1, "and", num2, "is", sum)#


# Loop through a list of exam scores and print grades based on a specific grading scale.
grades = [85, 92, 78, 99, 65]
for score in grades:
  if score >= 90:
    print(score, "is an A.")
  elif score >= 80:
    print(score, "is a B.")