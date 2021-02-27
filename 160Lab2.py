#160 Weekly Lab 2
#Maezy Haldeman: maezy.haldeman@und.edu


#Part 1
#Prompt for hours, minutes, seconds
hours = int(input('Enter number of hours: ' ))
minutes = int(input('Enter number of minutes: ' ))
seconds = int(input('Enter number of seconds: ' ))

print(hours, 'hours,', minutes, 'minutes,', seconds, 'seconds')

#Convert hours and minutes to seconds, add to seconds
totalSeconds = int((hours * 60 * 60) + (minutes * 60) + seconds )
print('Number of seconds: ', totalSeconds)



#Part 2
