''' 3 – String Representing Floating-Point Value '''

def validation(str):
    i = 0
    j = len(str) - 1

    count = 0

    # Iterating the string and checking for whitespace characters
    # Incrementing the counter if a whitespace character is found
    # Finally printing the count
    for a in str:
        if a.isspace() == True:
            count += 1
    if count > 0:
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

            # If last char is '.' or not digit then return false
            if i + 1 >= len(str):
                return False
            if not ('0' <= str[i+1] <= '9'):
                return False

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

number = input("Enter Number: ")

if validation(number):
    print("Valid Number")

else:
    print("Invalid Number")