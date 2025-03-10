""" This program will ask the user for their name and their favourite numbers 
    and then perform some simple maths on the numbers. """

#Ask the user for their name and favourite numbers
name = input("Whats your name? ")
num1 = int(input('What is your favourite number? '))
num2 = int(input('What is your second favourite number? '))

#Perform some simple maths on the numbers
add = num1 + num2
mulitply = num1*num2

#Greet user and print the results
print(f'Hi {name}, here are some fun calculations with your favourtie numbers:')
print(f'{add} is the result of both your favourite numbers added and {mulitply} is both your favourite numbers mulitplied.')
