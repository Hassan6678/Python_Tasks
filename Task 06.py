'''Sqaure Root'''

def squareroot(number):
    if number == 0:
        return 0

    # Step 1 --> take initial guess
    guess = number/2.0
    # Step 2 --> Take second guess2
    guess2 = guess + 1
    # Step 3
    while guess != guess2:
        n = number / guess
        guess2 = guess
        guess = (guess + n) / 2

    return guess


'''User Input'''
number = float(input("Enter Number for Square root: "))
print('The Square root of', number,': ', squareroot(number))
