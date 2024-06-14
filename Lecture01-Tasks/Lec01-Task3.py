# Task 3
# Print the calendar of a given month and year

import calendar

# Taking user input for year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Create a calendar object
cal = calendar.TextCalendar(calendar.SUNDAY)

# Generate the calendar for the given month and year
month_calendar = cal.formatmonth(year, month)

# Printing the calendar
print(month_calendar)
