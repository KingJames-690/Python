'''This program will ask the user to enter a sea level measurement. Once this is inputed the program will find the average and specify which of the measurements were greater than the average'''

#Create a looping list and ask to enter sea level input
measurements = []
sea_level = int(input('Enter sea level: '))
while sea_level:
  measurements.append(sea_level)
  sea_level = int(input('Enter sea level: '))
