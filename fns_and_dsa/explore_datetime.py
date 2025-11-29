#Part 1: Display the Current Date and Time

from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    format_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {format_date}")
    return current_date
current_date= display_current_datetime()

# Part 2: Calculate a Future Date
#prompt the user to enter a number of days (as an integer).
#Create a function with a name calculate_future_date and
#saves the future date inside a future_date variable
#Calculate what the date will be after adding the specified number of days to the current date.
#Print the future date in a format like “YYYY-MM-DD”.

# enter future date
enter_day = int (input("input the future day: "))
def calculate_future_date():
    future_date = current_date + timedelta(days=enter_day)
    formated_future_date = future_date.strftime("%Y-%m-%d")
    print(formated_future_date)
    return future_date
future_date = calculate_future_date()
print (f" Future date: {future_date}")







