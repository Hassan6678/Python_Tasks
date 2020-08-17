'''Take User Input as integer'''

no_of_adult = int(input("Number of adults: "))
no_of_children = int(input("Number of children: "))

count_family = 0
while no_of_adult >= 2 and no_of_children >= 2:
    no_of_adult = no_of_adult - 2
    no_of_children = no_of_children - 2
    count_family = count_family + 1

'''Cost of Tickets'''

cost_of_adult_ticket = 10   # 10$
cost_of_children_ticket = 5 # 5$
cost_of_family_ticket = 26  # 26$  Family(2 Adult & 2 Chilfren)


'''Total Cost Calculation'''

Total_Cost  = (no_of_adult * cost_of_adult_ticket) + (no_of_children * cost_of_children_ticket) + (count_family * cost_of_family_ticket)

'''Print Final Result In Dollar ($)'''
print('Number of family tickets: ',count_family)
print('Number of adult tickets: ',no_of_adult)
print('Number of child tickets: ',no_of_children)

print ('Total Cost: ${}'.format(Total_Cost))