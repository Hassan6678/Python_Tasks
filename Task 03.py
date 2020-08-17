''' 3 – String Representing Floating-Point Value '''

def check_number(str):
    i = 0
    j = len(str) - 1

    # Handling whitespaces
    while i < len(str) and str[i] == ' ':
        i += 1
    while j >= 0 and str[j] == ' ':
        j -= 1

    if i > j:
        return False

    # if string is of length 1 and the only
    # character is not a digit
    if i == j and not ('0' <= str[i] <= '9'):
        return False

    # If the 1st char is not '+', '-', '.' or digit
    if (str[i] != '.' and str[i] != '+' and
            str[i] != '-' and not ('0' <= str[i] <= '9')):
        return False

    ''' To check if a '.' or 'e' is found in given
    string.We use this flag to make sure that
    either of them appear only once. '''
    flag = False

    for i in range(j + 1):

        # If any of the char does not belong to
        # {digit, +, -,., e}
        if (str[i] != 'e' and str[i] != '.' and
                str[i] != '+' and str[i] != '-' and not
                ('0' <= str[i] <= '9')):
            return False
        if str[i] == '.':

            # check if the char e has already
            # occured before '.' If yes, return 0
            if flag:
                return False
            if i + 1 > len(str):
                return False
            if not ('0' <= str[i] <= '9'):
                return False
        elif str[i] == 'e':

            # set flagDotOrE = 1 when e is encountered.
            flag = True

            # if there is no digit before e
            if not ('0' <= str[i - 1] <= '9'):
                return False

            # if e is the last character
            if i + 1 > len(str):
                return False

            # if e is not followed by
            # '+', '-' or a digit
            if (str[i + 1] != '+' and str[i + 1] != '-' and
                    (str[i + 1] >= '0' and str[i] <= '9')):
                return False

    # If the string skips all the
    # above cases, it must be a numeric string
    return True


number = input("Enter Number: ")
print(check_number(number))