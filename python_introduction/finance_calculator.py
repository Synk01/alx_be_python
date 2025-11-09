# User Input for Financial Details
monthly_income = int(input ("Enter your monthly income: ")) 
# total monthly expenses: “Enter your total monthly expenses: ”.
monthly_expense = int(input ("Enter your monthly expenses: ")) 
# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expense
# Project Annual Savings
# Assume a simple annual interest rate of 5%.
# Calculate the projected savings after one year, incorporating the interest. 
# Use the simplified formula for annual savings projection: 
projected_savings = (monthly_savings  *  12 + (monthly_savings * 12 * 0.05))
# Display the user’s monthly savings.
print (f"projected savings after one year, with interest, is {projected_savings} ")
