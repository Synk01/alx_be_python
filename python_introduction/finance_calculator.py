# to  receive user input for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# simple annual interest rate
annual_interest_rate = 0.05

# to Calculate projected annual savings with interest
#  formula is (Monthly Savings * 12) + (Annual Interest on total savings)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Display the results
print("\n--- Financial Summary ---")
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings with interest are: ${projected_savings:.2f}")
