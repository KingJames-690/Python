'''This program will ask the user to enter a sea level measurement. Once this is inputed the program will find the average and specify which of the measurements were greater than the average'''

#Create a looping list and ask to enter sea levek input
todo_list = []
sea_level = int(input('Enter sea level: '))
while sea_level:
  todo_list.append(sea_level)
  sea_level = int(input('Enter sea level: '))

