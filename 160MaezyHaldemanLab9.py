'''
160 Computer Science 1: Online
Lab 9
Maezy Haldeman: maezy.haldeman@und.edu
ID#: 1325352

This program asks the user to select a text file from their device for reading.\
The fillListFromFile function reads the file and turns its contents into a list of ints.
The program then performs several functions on the list, finding and returning specific information. 

'''

import FileUtils
import os

#===========================================

#---------------- get list -----------------

def fillListFromFile(fileName):
    
    fileList = []
    
    if fileName == None: 
        
        print('No file selected. Exiting program...')
        os._exit(0)
        
    if os.path.isfile(fileName) == False: 
        print ("Entered file doesn't exist. Exiting program...")
        os._exit(0)
      
    else:    
    
        openFile = open(fileName, 'r')
        readToList = openFile.readlines()
        
        for element in readToList:
            fileList.append(int(element.strip()))
            
        openFile.close()
    
    return fileList    

#------------- get max value ---------------

def findMaxValue(theList):
    
    maxValue = None
    
    for number in theList:
        
        if maxValue == None:
            
            maxValue = number
        
        if number >= maxValue:
            
            maxValue = number
    
    return maxValue

#------------- get min value ---------------

def findMinValue(theList):
    
    minValue = None
    
    for number in theList:
        
        if minValue == None:
            
            minValue = number
            
        if number <= minValue:
            
            minValue = number
            
    return minValue

#------------- get the range ---------------

def intCalcRange(theList):
    
    rangeOfValues = findMaxValue(theList) - findMinValue(theList)
    
    return rangeOfValues

#------------ get the average --------------

def calcAverage(theList):
    
    total = 0
    sumNumbers = 0
    
    for number in theList:
        
        total += 1
        sumNumbers += number
        
    average = sumNumbers/total
    
    return average

#------ find numbers above given value ------

def findNumberAbove(theList, testValue):
    
    numberAbove = 0
    
    for number in theList:
        
        if number > testValue:
            
            numberAbove += 1
            
    return numberAbove

#---- find the first occurance of a value -----

def findFirstOccurance(theList, valueToFind):
    
    indexOccurance = -1
    firstOccurance = False
    
    for number in theList:
        
        indexOccurance += 1
        
        if number != valueToFind:
            
            firstOccurance = False
            continue
        
        elif number == valueToFind:
            
            firstOccurance = True
            break
            
    if firstOccurance == False:
        
        indexOccurance = -1
    
    return indexOccurance

#----- find the last occurance of a value ------

def findLastOccurance(theList, valueToFind):
    
    indexOccurance = -1
    lastOccurance = False
    Occurance = 0
    
    for number in theList:
        
        indexOccurance += 1
        
        if number == valueToFind:
                        
            lastOccurance = True
            Occurance = indexOccurance
                  
    if lastOccurance == False:
        
        indexOccurance = -1
        
    if lastOccurance == True:
        
        indexOccurance = Occurance
    
    return indexOccurance
    
#---- find the number of occurances of a value ----

def calcCount (theList, valueToFind):
    
    numOccurances = 0
    
    for number in theList:
        
        if number == valueToFind:
            
            numOccurances += 1
            
    return numOccurances

#------ find if the value is in the list ------

def isInList(theList, valueToFind):
    
    inTheList = False
    
    for number in theList:
        
        if number == valueToFind:
            
            inTheList = True
            
    return inTheList

#-------------------------------------------

#****************** main *******************

def main():
    
    print('Starting program...')
    print()
    
    print("Select data file for reading: ")
    fileName = FileUtils.selectSaveFile()
    print()
    
    theList = fillListFromFile(fileName)
    
    maxValue = findMaxValue(theList)
    print('Maximum value:', maxValue)
    
    
    minValue = findMinValue(theList)
    print('Minimum value:', minValue)
    
    
    rangeOfValues = intCalcRange(theList)
    print('Range of values:', rangeOfValues)
    
    
    averageOfValues = calcAverage(theList)
    print('Average of values:', averageOfValues)
    
    print()
    testValue = int(input('Enter a value: '))
    print()
    
    numberAbove = findNumberAbove(theList, testValue)
    print('Numbers above ', testValue, ': ', numberAbove, sep='')
    
    print()
    valueToFind = int(input('Enter a value: '))
    print()
    
    firstIndexOccurance = findFirstOccurance(theList, valueToFind)
    print("Index of value's first occurance: ", firstIndexOccurance)

    lastIndexOccurance = findLastOccurance(theList, valueToFind)
    print("Index of value's last occurance: ", lastIndexOccurance)
    
    numberOfOccurances = calcCount(theList, valueToFind)
    print('Number of occurances of ', valueToFind, ': ', numberOfOccurances, sep='')
    
    inTheList = isInList(theList, valueToFind)
    print('Is in the list:', inTheList)
    
    print()
    print('Exiting program...')   
    
#*******************************************
    
#===========================================

main()
    
    
    