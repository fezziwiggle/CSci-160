'''
Lab Exam 1 (Online)
Feb 27 2020: 8:00 AM
Maezy Haldeman: maezy.haldeman@und.edu
'''

print('Available flavors are: Vanilla, Chocolate, Strawberry, Neapolitan, and Pistachio.')
print()

#initializing variables
userFlavor = input('Enter your favorite flavor: ')
numStudents = 0

vanillaCount = 0
chocolateCount = 0
strawberryCount = 0
neapolitanCount = 0
pistachioCount = 0

vanillaPercent = 0
chocolatePercent = 0
strawberryPercent = 0
neapolitanPercent = 0
pistachioPercent = 0

#loop while a favorite flavor was entered
while len(userFlavor) != 0:
    
    #count for each flavor
    if userFlavor == 'Vanilla' or userFlavor == 'vanilla':
        vanillaCount += 1
    elif userFlavor == 'Chocolate' or userFlavor == 'chocolate':
        chocolateCount += 1  
    elif userFlavor == 'Strawberry' or userFlavor == 'strawberry':
        strawberryCount += 1    
    elif userFlavor == 'Neapolitan' or userFlavor == 'neapolitan':
        neapolitanCount += 1    
    elif userFlavor == 'Pistachio' or userFlavor == 'pistachio':
        pistachioCount += 1        
    
    numStudents += 1
    
    userFlavor = input('Enter your favorite flavor: ')

print()
    

#flavor percentages  
if numStudents != 0:
    vanillaPercent = (vanillaCount / numStudents) * 100
    chocolatePercent = (chocolateCount / numStudents) * 100
    strawberryPercent = (strawberryCount / numStudents) * 100
    neapolitanPercent = (neapolitanCount / numStudents) * 100
    pistachioPercent = (pistachioCount / numStudents) * 100
    
    
#displaying total students and stats for each flavor   
print('Total students:', numStudents)
print()

print('Number for Vanilla:', end='')
print(format(vanillaCount, ">14d"))
print('Percentage for Vanilla:   ', format(vanillaPercent,"1.3f"))
print()

print('Number for Chocolate:', end='')
print(format(chocolateCount, ">12d"))
print('Percentage for Chocolate: ', format(chocolatePercent, "1.3f"))

print()

print('Number for Strawberry:', end='')
print(format(strawberryCount, ">11d"))
print('Percentage for Strawberry:', format(strawberryPercent, "1.3f"))

print()

print('Number for Neapolitan:', end='')
print(format(neapolitanCount, ">11d"))
print('Percentage for Neapolitan:', format(neapolitanPercent, "1.3f"))

print()

print('Number for Pistachio:', end='')
print(format(pistachioCount, ">12d"))
print('Percentage for Pistachio: ', format(pistachioPercent, "1.3f"))

print()