'''This program will ask the user to enter a sea level measurement. Once this is inputed the program will find the average and specify which of the measurements were greater than the average'''

#Create a looping list
measurements = []

#Asking user for input and checking for valid input
while True:
    try:
        sea_level = int(input(f'Enter sea level: '))
        if sea_level >= 0:
            break
        else:
            print('Invalid input, please enter valid measurements.')
    except ValueError:
        print('Invalid input, please enter valid measurements.')
measurements.append(sea_level)

#When "over" is entered the loop must end. This block of code is for that
