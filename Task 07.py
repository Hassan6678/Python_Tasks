'''7 – Credit Card Checking '''

def valid_card(n):
    number = list(n)

    '''
    We will also take the number 43589795 as an example
    Starting from the rightmost digit, form the sum of of every other digit.
    For the example, the sum would be 5 + 7 + 8 + 3 = 23.
    '''
    num_1 = ""
    for i in range(1, len(number), 2):
        # Save this number this number
       num_1 += number[-1 * i]

    # Convert num_1 into integer list and Sum up all number
    num_1 = list(num_1)
    sum_num_1 = 0
    for num in num_1:
        sum_num_1 += int(num)

    '''
    • Double each of the digits that are not included in the preceding step.
    Add all the digits of the resulting numbers. For the example, we would
    take the digits 9, 9, 5, 4, and double them up to get 18, 18, 10, 8, and
    then add up the digits 1 + 8 + 1 + 8 + 1 + 0 + 8 = 27 
    '''
    num_2 = ""
    for i in range(0, len(number), 2):
        # Save this number this number
        num_2 += number[-1 * i]

    # Convert num_2 into integer list then double it and then Sum up all number
    num_2 = list(num_2)
    sum_num_2 = 0
    double_num_2 = ""
    for num in num_2:
        double_num_2 += str(int(num) * 2)

    double_num_2 = list(double_num_2)
    for num in double_num_2:
        sum_num_2 += int(num)

    '''
    • Add up the sums of the two preceding steps. If the last digit of the result
    is 0, the number is valid. For the example, we get 23 + 27 = 50, and
    the number is valid
    '''
    total_sum = sum_num_1 + sum_num_2
    if total_sum % 10 == 0:
        print("Valid Card Number")
    else:
        print("Error! Not Valid Card")



'''
Q: In the above example, the final check sum is 50, and therefore we conclude
that the credit card number is valid. What if the last digit of the check sum
is not 0. Can we determine what the check digit should be to make the credit
card number valid?
A: Yes, we can. Let CD denote the check digit and E denote the last digit of
the check sum. The check digit we want can be calculated as
new CD = (old CD - E + 10) %10
Try it out if you wish.
'''

def Extra(old_CD):
    # old_CD = total_sum --> as above calculated
    # E is last digit of old CD
    old_CD = str(old_CD)

    E = old_CD[-1]

    old_CD = int(old_CD)

    new_CD = (old_CD - int(E) + 10) % 10

    return new_CD



'''User Input'''
Card_number = str(input("Please Enter 8-digit of your Card :"))
valid_card(Card_number)
# print("n",Extra(45))