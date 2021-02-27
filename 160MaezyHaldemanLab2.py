#CSCI 160 Weekly Lab 2
#Maezy Haldeman: maezy.haldeman@und.edu


#Part 1
#prompt for hours, minutes, seconds
hours1 = int(input('Enter number of hours: ' ))
minutes1 = int(input('Enter number of minutes: ' ))
seconds1 = int(input('Enter number of seconds: ' ))

print(hours1, 'hours,', minutes1, 'minutes,', seconds1, 'seconds')

#convert hours and minutes to seconds, add to seconds
totalSeconds1 = int((hours1 * 60 * 60) + (minutes1 * 60) + seconds1 )

print('Number of seconds: ', totalSeconds1)
print()


#Part 2
#prompt for number of seconds
totalSeconds2 = int(input('Enter a number of seconds: '))

#convert total seconds to hours, minutes, and seconds
hours2 = totalSeconds2 // 3600
remainderSeconds = totalSeconds2 % 3600
minutes2 = remainderSeconds // 60
seconds2 = remainderSeconds % 60

print(totalSeconds2, 'seconds is:', hours2, 'hours, ', minutes2, 'minutes, ', seconds2, 'seconds.')
print()


#Part 3
#prompt for a number of quarters, dimes, nickels, amd pennies
quarters = int(input('Enter a number of quarters: '))
dimes = int(input('Enter a number of dimes: '))
nickels = int(input('Enter a number of nickels: '))
pennies = int(input('Enter a number of pennies: '))

#convert into cents
totalCents = ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies)
totalDollars = totalCents / 100.0

print(quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels, and', pennies, 'pennies is $', totalDollars)
print()


#Part 3
#prompt for words
print('Pet Show MadLib')

verbIng = input('Enter a verb ending with "-ing": ')
verbPast = input('Enter a past tense verb: ')
place = input('Enter a place: ')
adjective = input('Enter an adjective: ')
animalSing1 = input('Enter an animal (singular): ')
maleName = input('Enter a male name: ')
nounSing = input('Enter a singular noun: ')
verbPast2 = input('Enter a past tense verb: ')
animalSing2 = input('Enter an animal (singular): ')
number1 = input('Enter a number: ')
number2 = input('Enter another number: ')
nounPlur = input('Enter a plural noun: ')

print("While I was ", verbIng, " to the bus after school, ", sep='', end='')
print("I saw a poster announcing that a pet show would be held the next day in ", place, ". ", sep='', end='')
print("I was so ", adjective, "! ", sep='', end='')
print("I couldn't wait to enter my pet ", animalSing1, ",", maleName, ", in the show. ", sep='', end='')
print()
print("The next morning at the pet show, ", maleName, " balanced a big ", nounSing, "on his nose. ", sep='', end='')
print("Then he ", verbPast, " around three plastic ", nounPlur, ". ", sep='', end='')
print("Suddenly, a big ", animalSing2, " bumped into ", maleName, ". ", sep='', end='')
print("He ", verbPast2, " ", number1, " feet in the air. ", sep='', end='')
print("The judge made a terrible face when he saw what happened, so I didn't think ", maleName, " would win. ", sep='', end='')
print("Imagine my surprise when he won the number ", number2, " prize! ", sep='', end='')
print("I was happy to have a great ", animalSing1, " like ", maleName, ". ", sep='', end='')
                    
