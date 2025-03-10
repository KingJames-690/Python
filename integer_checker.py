""" This program will check to see if this user has entered a valid integer 
    in a specific range of values """

# Use constants for the low and high values
LOW = 1 
HIGH = 10

# Ask the user to type in a number
number = input('Please enter an integer ')

# CHeck to see if the number is valid
if number.lstrip('-').isnumeric():
  number = int(number)
  # Check to see if the number is iun the correct range
  if number < LOW:
    print(f'{number} is lower then {LOW}')
  elif number > HIGH:
    print(f'{number} is greater than {HIGH}')
  else:
    print(f'Your number is {number}')
else:
  print(f"{number} is not an integer")

# Make sure to test at least 5 different numerals