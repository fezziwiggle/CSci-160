'''
Maezy Haldeman, maezy.haldeman@und.edu
160: Computer Science I (ONLINE)
Weekly Lab 3
'''




#Part 1
print ('Part 1')
print()

#Numeric Value Tests
userNumber = float(input('Enter a number: '))
print()

#a) whole number or not
if (userNumber % 1) == 0:
    print (userNumber, 'is a whole number.')
else:
    print (userNumber, 'is not a whole number.')

#b) multiple of 5 or not
if (userNumber % 5) == 0:
    print (userNumber, 'is a multiple of 5.')
else:
    print (userNumber, 'is not a multiple of 5.')

#c) even or odd
if (userNumber % 2) == 0:
    print (userNumber, 'is even.')
else:
    print (userNumber, 'is odd.')

#d) positive, negative, or zero
if userNumber > 0:
    print (userNumber, 'is positive.')
elif userNumber < 0:
    print (userNumber, 'is negative.')
else:
    print (userNumber, 'is zero.')

#e) within 2010-2019
if 2010 <= userNumber <= 2019:
    print (userNumber, 'is within the range of 2010 and 2019 inclusive.')
else:
    print (userNumber, 'is not within the range of 2010 and 2019 inclusive.')

#f) within 100's
if 100 <= userNumber <= 199:
    print (userNumber, "is within the 100's.")
else:
    print (userNumber, "is not within the 100's.")

print()

#String Value Tests
userString = input('Enter a word: ')
print()

#g) how many characters
print ('"', userString, '" is ', len(userString), ' characters long.', sep='')

#h) if the string is "yes" or "no"
if userString == 'yes' or userString == 'YES':
    print ('"', userString, '" is "yes" or "YES".', sep='')
elif userString == 'no' or userString == 'NO':
    print ('"', userString, '" is "no" or "NO".', sep='')
else:
    print ('"', userString, '" is not "yes", "YES", "no", or "NO".', sep='')

#i) if the string is "yes" in lowercase or uppercase
if userString == 'yes':
    print ('"', userString, '" is lowercase.', sep='')
elif userString == 'YES':
    print ('"', userString, '" is uppercase.', sep='')
else:
    print ('"', userString, '" is neither uppercase or lowercase "yes".', sep='')

#j) if the string starts with an "a"
if userString[0] == 'a':
    print ('"', userString, '" starts with a lowercase "a".', sep='')
else:
    print ('"', userString, '" does not start with a lowercase "a".', sep='')
print()
print()





#Part 2
print ('Part 2')
print()

#user prompt
userValue = input('Enter a number between 0 and 99: ')


#if the user number has a tens place and a ones place
if len(userValue) == 2:
    
    tensDigit = int(userValue[0])
    
    onesDigit = int(userValue[1])
    
    if tensDigit != 1:
       
        #20-99 tens place
        tensWord = ''
        
        if tensDigit == 2:
            tensWord = 'twenty'
        elif tensDigit == 3:
            tensWord = 'thirty'
        elif tensDigit == 4:
            tensWord = 'forty'
        elif tensDigit == 5:
            tensWord = 'fifty'
        elif tensDigit == 6:
            tensWord = 'sixty'
        elif tensDigit == 7:
            tensWord = 'seventy'
        elif tensDigit == 8:
            tensWord = 'eighty'
        elif tensDigit == 9:
            tensWord = 'ninety'
        
        #20-99 ones place
        onesWord = ''
        
        if onesDigit == 1:
            onesWord = 'one'
        elif onesDigit == 2:
            onesWord = 'two'
        elif onesDigit == 3:
            onesWord = 'three'
        elif onesDigit == 4:
            onesWord = 'four'
        elif onesDigit == 5:
            onesWord = 'five'
        elif onesDigit == 6:
            onesWord = 'six'
        elif onesDigit == 7:
            onesWord = 'seven'
        elif onesDigit == 8:
            onesWord = 'eight'
        elif onesDigit == 9:
            onesWord = 'nine'
        elif onesDigit == 0:
            onesWord = ''
            
        
        print ('The number is', tensWord, onesWord)
        
    #10-19 teens    
    elif tensDigit == 1:
        
        if onesDigit == 0:
            teenWord = 'ten'
        elif onesDigit == 1:
            teenWord = 'eleven'
        elif onesDigit == 2:
            teenWord = 'twelve'
        elif onesDigit == 3:
            teenWord = 'thirteen'
        elif onesDigit == 4:
            teenWord = 'fourteen'
        elif onesDigit == 5:
            teenWord = 'fifteen'
        elif onesDigit == 6:
            teenWord = 'sixteen'
        elif onesDigit == 7:
            teenWord = 'seventeen'
        elif onesDigit == 8:
            teenWord = 'eighteen'
        elif onesDigit == 9:
            teenWord = 'nineteen'
        
        print ('The number is', teenWord)
        

#if the user number has only a ones place
elif len(userValue) == 1:
    
    singleDigit = int(userValue[0])
    
    if singleDigit == 0:
        singleWord = 'zero'
    if singleDigit == 1:
        singleWord = 'one'
    elif singleDigit == 2:
        singleWord = 'two'
    elif singleDigit == 3:
        singleWord = 'three'
    elif singleDigit == 4:
        singleWord = 'four'
    elif singleDigit == 5:
        singleWord = 'five'
    elif singleDigit == 6:
        singleWord = 'six'
    elif singleDigit == 7:
        singleWord = 'seven'
    elif singleDigit == 8:
        singleWord = 'eight'
    elif singleDigit == 9:
        singleWord = 'nine'
    
    print ('The number is', singleWord)
    
else:
    print ('That number is not within valid range.')
    
print()
print()





#Part 3
print('Part 3')
print()

#user prompt
creditsToDate = int(input('Enter the number of credits you have earned to date: '))
creditsInProgress = int(input('Enter the number of credits you are taking this semester: '))
print()

#current class status
if 0 <= creditsToDate <= 23:
    currentStatus = 'Freshman'
elif 24 <= creditsToDate <= 59:
    currentStatus = 'Sophomore'
elif 60 <= creditsToDate <= 89:
    currentStatus = 'Junior'
elif 90 <= creditsToDate:
    currentStatus = 'Senior'
    
print('You are a ', currentStatus, '.', sep='')

#anticipated class status
if 0 <= creditsToDate + creditsInProgress <= 23:
    anticipStatus = 'Freshman'
elif 24 <= creditsToDate + creditsInProgress <= 59:
    anticipStatus = 'Sophomore'
elif 60 <= creditsToDate + creditsInProgress <= 89:
    anticipStatus = 'Junior'
elif 90 <= creditsToDate + creditsInProgress:
    anticipStatus = 'Senior'
    
print('You will be a', anticipStatus, 'after this semester.')

#credits needed to graduate
gradCredits = 120 - (creditsToDate + creditsInProgress)

print('You need', gradCredits, 'more credits to graduate.')

#semesters needed if you take 15 credits/sem
import math

additionalSem = math.ceil(gradCredits / 15)

print('It will take', additionalSem, 'more semesters to graduate if you take 15 credits per semester.')


