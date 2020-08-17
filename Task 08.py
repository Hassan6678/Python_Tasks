"""a. Define a function called isLeapYear that takes a year as an integer and
returns True if it is a leap year and False otherwise.
A year, between 1800 and 20000, is a leap year if
• It is divisible by 4 but not by 100 or
• It is divisible by 400
For this function, you can assume that the year is between 1800 and 20000.
You do not need to check it.
"""
# Part (a)
def isLeapyear(year):
    # First Condition divisible by 4 but not 100
    if year % 4 == 0 and year % 100 != 0:
        return True
    # Second Condition divisible by 400
    if year % 400 == 0:
        return True
    return False


'''User Input'''
print("Part (a)\n")
year = int(input("Enter Year (between 1800 t0 20000): "))
if 1800 <= year <= 20000:
    if isLeapyear(year):
        print("Leap year")
    else:
        print("Not Leap year")
else:
    print("You enter Invalid year")

#Part(b)
"""b. Define a function called daysInMonth that takes a month of a year and
returns the number of days for that month. The function takes an integer
for the month (1 for January, 2 for February, etc.) and a year (an integer
between 1800 and 20000).
For this function, you can assume that the month is between 1 and 12 and
the year is between 1800 and 20000. You do not need to check them.
"""
from calendar import monthrange
def dayinMonth(year,month):
    num_days = monthrange(year, month)[1] # num_days
    print(num_days)

'''User Input'''
print("Part (b) Day in Month\n")
year = int(input("Enter year (between 1800 t0 20000): "))
month = int(input("Enter month (between 1 t0 12): "))
if 1800 <= year <= 20000:
    if 1 <= month <= 12:
        dayinMonth(year, month)
    else:
        print("Invalid month")
else:
    print("Invalid year")




# part (c)
"""c. Define a function called isValidDate that takes three integers for a day,
a month and a year (in that order) and returns True if the thee integers
represent a valid date and False otherwise.
"""

def date_validation(day, month, year):
    import datetime
    ValidDate = True

    try:
        datetime.datetime(int(year),int(month), int(day))

    except ValueError:
        ValidDate = False

    if (ValidDate):
        print("you Enter Valid Date")
        return True
    else:
        print("You Enter Wrong Date")
        return False


'''User Input'''
print("Part (c) date Validation\n")
year = int(input("Enter year (between 1800 t0 20000 : "))
month = int(input("Enter month (between 1 t0 12 : "))
day = int(input("Enter day (between 1 t0 31 : "))

date_validation(day, month, year)


# Part (d)
"""Write a function called dayOfWeek that takes the day, month and year of a
date and returns a number to represent the day of the week for that date,
with 0 for Monday, 1 for Tuesday and so on (Note the slight difference
from the outcome of Gauss’s algorithm).
If the numbers do not represent a valid date the function should return
None.
"""
def DayofWeek(year, month, day):
    import datetime
    ValidDate = True

    try:
        datetime.datetime(int(year), int(month), int(day))

    except ValueError:
        ValidDate = False

    if (ValidDate):
        x = int(year - (14 - month) / 12)
        y = int(x + x / 4 - x / 100 + x / 400)
        z = int(month + 12 * ((14 - month) / 12) - 2)
        dow = int((day + y + (31 * z) / 12) % 7)

        return dow - 1
    else:
        return None

'''User Input'''
print("Part (d) Day of Week\n")
year = int(input("Enter year (between 1800 t0 20000 : "))
month = int(input("Enter month (between 1 t0 12 : "))
day = int(input("Enter day (between 1 t0 31 : "))

print("Day of week :",(DayofWeek(year, month, day)))




# Part (e)
"""e. Write a function called printCalendar that takes two integers to represent
a particular month in a particular year and prints out the calendar for that
month.
"""
def printCalender(year,month):
    import calendar
    print(calendar.month(year, month))


'''User Input'''
print("Part (e) Calender Print\n")
year = int(input("Enter year (between 1800 t0 20000 : "))
month = int(input("Enter month (between 1 t0 12 : "))
if 1800 <= year <= 20000:
    if 1 <= month <= 12:
        printCalender(year, month)
    else:
        print("you Enter Invalid year")
else:
    print("you Enter Invalid month")


# Part (f)
"""f. Add statements to your program to ask the user for a birth date of a person
(day, month and year).
"""
def BirthDay(year, month, day):
    import datetime
    ValidDate = True

    try:
        datetime.datetime(int(year), int(month), int(day))

    except ValueError:
        ValidDate = False

    if (ValidDate):
        x = int(year - (14 - month) / 12)
        y = int(x + x / 4 - x / 100 + x / 400)
        z = int(month + 12 * ((14 - month) / 12) - 2)
        dow = int((day + y + (31 * z) / 12) % 7)

        return dow - 1
    else:
        return None

Day_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

'''User Input'''
print("Part (f) BirthDay\n")
year = int(input("Enter year (between 1800 t0 20000 : "))
month = int(input("Enter month (between 1 t0 12 : "))
day = int(input("Enter day (between 1 t0 31 : "))

print("The person was born on a", Day_array[(BirthDay(year, month, day))])