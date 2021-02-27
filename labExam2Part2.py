'''
Maezy Haldeman: maezy.haldeman@und.edu
CS160: Computer Science 1
Lab Exam 2 Part 2
ID#: 1325352

This program takes the user's selected file and reads its contents into a list. 
The program then tells the user the average of the scores in the list, the number of scores
in the list, the number of passing scores in the list, and then displays a table containing
the each score per student from the list.

'''

import FileUtils
import os

#===============================

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

#--------------------------------

def getClassPerformance(classAverage):
    
    if classAverage >= 90:
        
        classPerformance = 'The class did extremely well.'
         
    elif classAverage >= 70:
        
        classPerformance = 'The class did well.'
        
    else:
        
        classPerformance = 'The teacher needs to do better.'
        
    return classPerformance

#--------------------------------

def calcClassAverage(theList):
    
    numScores = 0
    scoreTotal = 0
    
    for score in theList:
        
        scoreTotal += score
        numScores += 1
        
    classAverage = scoreTotal / numScores
    
    return classAverage

#--------------------------------

def getNumStudents(theList):
    
    numStudents = 0
    
    for score in theList:
        
        numStudents += 1
        
    return numStudents

#--------------------------------

def numThatPassed(theList):
    
    numStudentsPassed = 0
    
    for score in theList:
        
        if score >= 70:
            
            numStudentsPassed += 1
            
    return numStudentsPassed

#--------------------------------

def printPercents(theList):
    
    studentNumber = 0
    
    header = ('------------------------------')
    footer = ('------------------------------')
    
    print(header)
    print('Student Number:', end='')
    print(format('Percentage:', '>15s'))
    
    for score in theList:
        
        studentNumber += 1
        
        print((format(studentNumber, '>14d')), end='') 
        print(format(score, '>15d'))
        
        
    return footer

#--------------------------------
#********************************

def main():

    print("Select data file: ")
    fileName = FileUtils.selectSaveFile()
    print()
    
    theList = fillListFromFile(fileName)
    
    classAverage = calcClassAverage(theList)
    
    classPerformace = getClassPerformance(classAverage)
    print(classPerformace)
    print()    
    
    print('Class average:', classAverage)

    numStudents = getNumStudents(theList)
    print('Number of students in class:', numStudents)
    
    numStudentsPassed = numThatPassed(theList)
    print('Number of students who passed:', numStudentsPassed)
    print()
    
    percentTable = printPercents(theList)
    print(percentTable)
    
#================================

main()
