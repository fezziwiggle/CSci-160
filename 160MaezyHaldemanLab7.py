'''
Maezy Haldeman: maezy.haldeman@und.edu
ID #: 1325352
CSCI 160: Computer Science I
Weekly Lab 7

This program defines functions to calculate the square, summation, sum of squares, and factorial for
any positive integer given by the user, as well as determines whether said integer is even or odd. 
The program also asks the user for four points, two sets of (x, y) coordinates, and defines a function 
to calculate the distance between these points.

'''

import math

#==================== Begin defining functions ====================

'''
This function squares the value of whatever the argument is.
The parameter is the user's input integer.
The return value is the square of the user's integer.
'''

def square(intValue):
    
    squareInt = ( intValue ** 2 )
    return squareInt

#------------------------------------------

'''
This function adds all the integers in the range of the argument.
The parameter is the user's input integer.
The return value is the the sum of all the integers in the range of the user's integer.
'''

def summation(intValue):
    
    summationInt = sum(range(intValue + 1))
    return summationInt

#------------------------------------------

'''
This function adds the squares of every integer in the range of the argument.
The parameter is the user's input integer.
The return value is the sum of all the squares of every integer in the range of the user's integer.
'''

def sumOfSquare(intValue):
    
    sumOfSquareInt = 0
    
    for num in range(intValue + 1):
        
        squareNum = ( num ** 2 )
        sumOfSquareInt += squareNum
        
    return sumOfSquareInt

#------------------------------------------

'''
This function multiplies all the integers in the range of the argument.
The parameter is the user's input integer.
The return value is the product of the integers in the range of the user's integer.
'''

def factorial(intValue):
    
    factorial = 1
    
    for num in range(1, intValue + 1):
        
        factorial = factorial * num
        
    return factorial

#------------------------------------------

'''
This function calculates the distance between the two points (x1, y1) and (x2, y2).
The parameter is the user's input for x1, y1, x2, and y2.
The return value is the distance between the two points specified by the user's input for x1, y1, x2, and y2.
'''

def distance(x1, y1, x2, y2):
    
    distance = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
    return distance

#------------------------------------------

'''
This function determines if the argument is odd.
The parameter is the user's input integer.
The return value is True if the user's integer is odd, or False if the user's integer is even.
'''

def isOdd(intValue):
    
    if intValue % 2 == 0:
        isOdd = False 
    else:
        isOdd = True

    return isOdd
    
#------------------------------------------

'''
This function determines if the argument is even.
The parameter is the user's input integer.
The return value is True if the user's integer is even, or False if the user's integer is odd.
'''

def isEven(intValue):
    
    if isOdd(intValue) == False:
        isEven = True
    else:
        isEven = False

    return isEven    
    
#========== Ask for user's integer and call related functions ========== 

intValue = int(input('Enter a positive integer: '))

print()

print('The square of', intValue, 'is', square(intValue))
print('The summation of', intValue, 'is', summation(intValue))
print('The sum of the squares of', intValue, 'are', sumOfSquare(intValue))
print('The factorial of', intValue, 'is', factorial(intValue))
if isOdd(intValue) == True:
    print(intValue, 'is odd')
if isEven(intValue) == True:
    print(intValue, 'is even')
    
print()

#========== Ask for user's points for (x1, y1) and (x2, y2) and call related function ========== 


x1 = int(input('Enter the x-value of the first point: '))
y1 = int(input('Enter the y-value of the first point: '))
x2 = int(input('Enter the x-value of the second point: '))
y2 = int(input('Enter the y-value of the second point: '))

print()

print('The distance between (', x1, ',', y1, ') and (', x2, ',', y2,') is ', distance(x1, y1, x2, y2), sep='')
