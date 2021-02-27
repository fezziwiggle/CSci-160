'''
160: Computer Science I (ONLINE)
Weekly Lab 4
Maezy Haldeman: maezy.haldeman@und.edu
'''


#Part A
print('Part A')
print()

#1) 10 to 50 by 1
print('Part 1')
print()

counter1 = 10
endValue1 = 50

while counter1 <= endValue1:
    print(counter1)
    counter1 += 1
    
print()
    
#2) 20 to 0 by 1
print('Part 2')
print()

counter2 = 20
endValue2 = 0

while counter2 >= endValue2:
    print(counter2, end=' ')
    counter2 -= 1
    
print()
print()

#3) 0 to 10 by 0.5
print('Part 3')
print()

counter3 = 0
endValue3 = 10

while counter3 <= endValue3:
    print(counter3)
    counter3 += 0.5
    
print()

#4) alphabet echoing 
print('Part 4')
print()

userLetter = input('Enter a letter: ')
endValue4 = 'q' or 'Q'
numLowercase = 0
numUppercase = 0

while userLetter != endValue4:
    if 'A' <= userLetter <= 'Z':
        numLowercase += 1
    if 'a' <= userLetter <= 'z':
        numUppercase += 1
    print('You entered ', "'", userLetter, "'", sep='')
    userLetter = input('Enter a letter: ')
    
print()
    
print('You entered', numLowercase, 'lowercase letters.')
print('You entered', numUppercase, 'uppercase letters.')

print()
print()


#Part B
print('Part B')
print()

lineLength = 1
userLength = int(input('Enter a length for a line: '))
print()

while lineLength <= userLength:
    print('*', end='')
    
    lineLength += 1

print()
print()
print()

#Part C
print('Part C')
print()

userInt = int(input('Enter an integer value (enter \'0\' when you want to quit): '))

positiveList = []
negativeList = []
numPositive = 0
numNegative = 0

if userInt != 0:
    while userInt != 0:
        
        if userInt >= 1:
            numPositive += 1
            positiveList.append(userInt)
            
        elif userInt <= -1:
            numNegative += 1
            negativeList.append(userInt)
            
        userInt = int(input('Enter an integer value: '))

    if numPositive != 0:
        avgPositive = (sum(positiveList)) / numPositive
    else:
        avgPositive = 0
    
    if numNegative != 0:
        avgNegative = (sum(negativeList)) / numNegative
    else:
        avgNegative = 0

    print()
    
    print('Average of positive values:', avgPositive)
    print('Average of negative values:', avgNegative)

else:
    print('You have exited the program.')

print()
print()

#Part D
print('Part D')
print()

userNum = int(input('Enter a number between 1 and 10: '))
print() 

multiplier = 1
product = ''

print('Multiplication table for', userNum)
print()

if 1 <= userNum <= 10:
    
    while 1 <= multiplier <= 10:
        
        product = multiplier * userNum
        
        if len(str(product)) == 1:
            print(format( (str(multiplier) + ' * ' + str(userNum) + ' =  ' + str(product)), '>12s'))
        else:
            print(format( (str(multiplier) + ' * ' + str(userNum) + ' = ' + str(product)), '>12s'))
            
        multiplier += 1
    
else:
    print('That input is not valid.')


    

                


