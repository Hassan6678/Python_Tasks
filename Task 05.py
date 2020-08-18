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
    '''
    Seperate number into 2 parts like
    If number is 12.21 then
    d = 12.0 # decimal part
    f = 0.21 # fraction part
    '''
    d = number // 1
    f = round(number % 1, 2)

    # Now we Round off over Fraction part according to Given rules...
    # convert fraction into decimal
    f = f * 100
    # Now check fraction part turn by turn
    if f == 0.0:
        # Only Deal with Decimal part
        # Typecasting --> convert float decimal into int Decimal
        d = int(d)
        # Casting int to String to get the last digit from decimal number
        d = str(d)
        # Extract last digit from our Decimal number
        last = d[-1]
        # re cast into into to performing roundoff function
        last = int(last)
        # Special Case if last == 10 then What we Do
        # then we update second last digit
        if adjust(last) == 10:
            # extract second last digit
            second_last = d[-2]
            second_last = int(second_last)
            second_last = second_last + 1
            second_last = str(second_last)
            new_d = list(d)
            new_d[-1] = '0'
            new_d[-2] = second_last
            # initialize an empty string
            str1 = ""

            # traverse in the string
            for ele in new_d:
                str1 += ele

            new_d = float(str1)
            print("New: ", new_d)
        else:
            # if last digit is 0 or 5 then
            last_digit = adjust(last)
            last_digit = str(last_digit)
            new_d = list(d)
            new_d[-1] = last_digit
            # initialize an empty string
            str1 = ""

            # traverse in the string
            for ele in new_d:
                str1 += ele

            new_d = float(str1)
            print("New: ", new_d)

    else:

        # Typecasting --> convert float decimal into int Decimal
        f = int(f)
        # Casting int to String to get the last digit from decimal number
        f = str(f)
        # Extract last digit from our Decimal number
        last = f[-1]
        # re cast into into to performing roundoff function
        last = int(last)
        # Special Case if last == 10 then What we Do
        # then we update second last digit
        if adjust(last) == 10:
            # extract second last digit
            second_last = f[-2]
            second_last = int(second_last)
            second_last = second_last + 1
            second_last = str(second_last)
            new_f = list(f)
            new_f[-1] = '0'
            new_f[-2] = second_last
            # initialize an empty string
            str1 = ""

            # traverse in the string
            for ele in new_f:
                str1 += ele

            new_f = float(str1)
            new_f = new_f / 100
            new_num = d + new_f
            print("New: ", new_num)
        else:
            # if last digit is 0 or 5 then
            last_digit = adjust(last)
            last_digit = str(last_digit)
            new_f = list(f)
            new_f[-1] = last_digit
            # initialize an empty string
            str1 = ""

            # traverse in the string
            for ele in new_f:
                str1 += ele

            new_f = float(str1)
            new_f = new_f / 100
            new_num = d + new_f
            print("New: ", new_num)






# The amount is entered as a decimal number with 0, 1 or 2 decimal places.

number = float(input("Enter: "))


roundOff(number)