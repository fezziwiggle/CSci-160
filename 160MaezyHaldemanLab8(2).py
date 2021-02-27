'''
160 Computer Science 1: Online
Lab 8 Part 2
Maezy Haldeman: maezy.haldeman@und.edu
ID#: 1325352

'''

import FileUtils
import os

fileNumList = []

#==================== defining functions ====================

def getFileNumList(fileName):
    
    openFile = open(fileName, 'r')
    fileStringList = openFile.readlines()
    
    for element in fileStringList:
        fileNumList.append(int(element.strip()))
        
    openFile.close()
    
    return fileNumList

#----------------------------------------------

def getLargestNum(fileNumList):
    
    largestNum = 0
    
    for number in fileNumList:
        
        if number >= largestNum:
            largestNum = number
            
    return largestNum
    
#----------------------------------------------

def getSmallestNum(fileNumList):
    
    smallestNum = 0
    
    for number in fileNumList:
        
        if smallestNum == 0:
            smallestNum = number        
        
        elif number <= smallestNum:
            smallestNum = number
            
    return smallestNum

#----------------------------------------------

def getAverageNum(fileNumList):
    
    sumNum = 0
    totalNum = 0
    
    for number in fileNumList:
        sumNum += number
        totalNum += 1
    
    averageNum = format((sumNum / totalNum), "1.2f")
    
    return averageNum    

#----------------------------------------------

def getMatchingValues(fileNumList, lowerLimit, upperLimit):
    
    rangeNumList = []
    
    for number in fileNumList:
        
        if lowerLimit <= number <= upperLimit:
            
            rangeNumList.append(number)
            
    rangeNumList.sort()
            
    print('Matching values:', rangeNumList)          

#--------------------- main ---------------------

def main():

    print("Select data file: ")
    fileName = FileUtils.selectSaveFile()
    print()
    
    if fileName == None: 
        
        print('No file selected. Exiting program...')
        os._exit(0)
        
    if os.path.isfile(fileName) == False: 
        print ("Entered file doesn't exist")
        os._exit(0)
        
    else: 
        
        myList = getFileNumList(fileName)
        print('Largest score:', getLargestNum(myList))
        print('Smallest score:', getSmallestNum(myList))
        print('Average score:', getAverageNum(myList))
        
        print()
        
        print('Enter a range of values')
        lowerLimit = int(input('Enter the lower limit: '))
        upperLimit = int(input('Enter the upper limit: '))
        getMatchingValues(myList, lowerLimit, upperLimit)    
        
#==========================================

main()