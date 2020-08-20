''' 3 – String Representing Floating-Point Value '''

def validation(str):
    i = 0
    j = len(str) - 1

    count = 0

    # Iterating the string and checking for whitespace characters
    # Incrementing the counter if a whitespace character is found
    # Finally return false
    for a in str:
        if a.isspace() == True:
            count += 1
    if count > 0:
        return False

    # counting '.'
    count_dot = 0
    for dot in str:
        if dot == '.':
            count_dot += 1
    if count_dot > 1:
        return False

    # counting '-'
    count_minus = 0
    for minus in str:
        if minus == '-':
            count_minus += 1
    if count_minus > 1:
        return False

    # counting '+'
    count_plus = 0
    for plus in str:
        if plus == '+':
            count_plus += 1
    if count_plus > 1:
        return False

    # Check if '-' appear after 1st place like '12-'
    count_min = 0
    for min in range(1,len(str)):
        if str[min] == '-':
            count_min += 1
    if count_min > 0:
        return False

    # Check if '+' appear after 1st place like '12-'
    count_p = 0
    for p in range(1,len(str)):
        if str[p] == '+':
            count_p += 1
    if count_p > 0:
        return False

    # if string is of length 1 and the only
    # character is not a digit
    if i == j and not ('0' <= str[i] <= '9'):
        return False

    # If the 1st char is not '+', '-', '.' or digit
    if (str[i] != '.' and str[i] != '+' and
            str[i] != '-' and not ('0' <= str[i] <= '9')):
        return False

    # To check if a '.' or 'e' is found in given
    # string.We use this flag to make sure that
    # either of them appear only once.

    flag = False

    for i in range(j+1):

        # If any of the char does not belong to {digit, +, -,., e}
        if (str[i] != 'e' and str[i] != '.' and
                str[i] != '+' and str[i] != '-' and not
                ('0' <= str[i] <= '9')):
            return False

        if str[i] == '.':

            # check if the char e has already occurred before '.' If yes, return false
            if flag:
                return False

            # If last char is '.' return True
            if i + 1 >= len(str):
                return True
            # if last char is not digit then return false
            # if not ('0' <= str[i+1] <= '9'):
            #     return False

        elif str[i] == 'e':

            # set flagDotOrE = 1 when e is encountered.
            flag = True

            # if there is no digit before e (if last chr is '.')
            if not ('0' <= str[i - 1] <= '9'):
                return False

            # if e is the last character
            if i + 1 >= len(str):
                return False

            # if e is not followed by
            # '+', '-' or a digit
            if str[i + 1] != '+' and str[i + 1] != '-' and (str[i + 1] >= '0' and str[i] <= '9'):
                return False

    # If the string skips all the
    # above cases, it must be a numeric string
    return True


#  case reported by Haider
# 1.   --1.9
print(validation('--1.9')) # False
# 2.   .123.45
print(validation('.123.45')) # False
# case that count my Hassan
# 1.   -.12
print(validation('-.12')) # True
# 2.   +-1 or + -+1
print(validation('-+.1')) # True
# 3.    12.12- , 12- , 12+ ?
print(validation('12.12-')) # False
# 4.     123.
print(validation('12.')) # True

number = input("Enter Number: ")

if validation(number):
    print("Valid Number")

else:
    print("Invalid Number")
