'''This program will ask the user how many of the toppings the user would like on their pizza, skipping any toppings which have not been ordered. The order must be printer'''

#Create a list of pizza options
pizza = ['cheese', 'chicken', 'pepperoni', 'veggies']

#Create list to store how many of each pizza
quantities = []

#Go through list of pizza options
for toppings in pizza:
    #Ask how many of each pizza
    howmany = input( f'How many {toppings} pizzas do we want? ')
    quantities.append(howmany)

print(quantities)