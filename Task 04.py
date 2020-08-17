'''4 – Millionaire Plan '''

"""Bob has a plan to be a millionaire. In month 1, he saves 1 dollar. In month 2,
he saves 2 dollars. In month 3, he saves 4 dollars, and so on. In general, for
each month, he saves twice the amount of the previous month.
"""

# Part(a)
# How much money will Bob save after 1 year (12 months)?
total_moeny = 0  # at start
year = 12  # has 12 month
money = 1
# loop ( Starting from 1 and end at 13)
for month in range(1, year+1):
    # Calculate Money over 12 Month
    total_moeny = money + total_moeny
    money = money * 2


'''Print Final Result In Dollar ($)'''
print('\nTotal Money that Bob save after 1 year: ${}'.format(total_moeny))

print('\n')

# Part (b)
# When (after how many months) he will become a millionaire ?
total_moeny = 0  # at start
money = 1
count_month = 0
# loop ( Starting from 1 and end at 13)
while total_moeny <= 1000000: # 1 Million = 10,00000 (10 lac )
    # Calculate Money over 12 Month
    total_moeny = money + total_moeny
    money = money * 2
    count_month = count_month + 1

print('Bob will become a millionaire after {} months.'.format(count_month))