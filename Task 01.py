#Bis Mil Allah

'''Take User Input as integer'''

no_of_adult = int(input("Number of adults: "))
no_of_children = int(input("Number of children: "))
no_of_family_ticket = int(input("Number of family tickets: "))
no_of_adult_ticket = int(input("Number of adult tickets: "))
no_of_child_tickets = int(input("Number of child tickets: "))

'''Cost of Tickets'''

cost_of_adult_ticket = 10   # 10$
cost_of_children_ticket = 5 # 5$
cost_of_family_ticket = 26  # 26$  Family(2 Adult & 2 Chilfren)


'''Total Cost Calculation'''

Total_Cost  = (no_of_adult_ticket * cost_of_adult_ticket) + (no_of_child_tickets * cost_of_children_ticket) + (no_of_family_ticket * cost_of_family_ticket)

'''Print Final Result In Dollar ($)'''
print ('Total Cost: ${}'.format(Total_Cost))