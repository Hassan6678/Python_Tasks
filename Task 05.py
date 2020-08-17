''' 5 – Rounding to Nearest Five Cents '''
"""

a. Write a function, named adjust, that takes a number of cents between 0
and 9, inclusive, rounds it off to the nearest 5 cents by the following rules,
and returns the result:
• 1 and 2 cents are rounded off to 0
• 3, 4, 6 and 7 cents are rounded off to 5
• 8 and 9 cents are rounded off to 10 cents
"""
# Part (a)
def adjust(cent):
    if cent == 1 or cent == 2:
        cent = 0
        return cent
    if cent == 3 or cent == 4 or cent == 6 or cent == 7:
        cent = 5
        return cent
    if cent == 8 or cent == 9:
        cent = 10
        return cent
    else:
        return cent

"""
b. Write a function, named roundOff, that takes an amount of money in
dollars, and rounds it off to the nearest 5 cents and returns the result. The
amount is entered as a decimal number with 0, 1 or 2 decimal places. The
rounding off is based on the rules given above.
"""
# Part (b)
def roundOff(number):
    # Check the number is Integer or float
    if number.is_integer():
        print(number)





number = float(input("Enter: "))
roundOff(number)