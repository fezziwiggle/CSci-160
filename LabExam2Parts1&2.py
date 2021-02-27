'''
Maezy Haldeman: maezy.haldeman@und.edu
CS160: Computer Science 1
Lab Exam 2 Parts 1 & 2
ID#: 1325352

Part 1 of this program asks the user for the number of students in a class,
then requests a score for each student. The program then asks the user
to select a file, and then saves the scores to that file.

Part 2 of this program takes the user's selected file and reads its contents into a list. 
The program then tells the user the average of the scores in the list, the number of scores
in the list, the number of passing scores in the list, and then displays a table containing
the each score per student from the list.

'''

import FileUtils
import os

#===========================================

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


#---------------- Part 1 -------------------

def main():
    
    print('PART ONE')   
    print()
    
    studentScores = []
    numStudents = int(input('Enter the number of students in the class: '))
    print()
    
    for student in range(1, numStudents+1):
        
        studentPercent = input('Enter a percentage for student ' + str(student) + ': ')
        
        if 0 <= int(studentPercent) <= 100:
        
            studentScores.append(studentPercent)
        
    #print(studentScores)
    
    print()
    
    print('Select a name for the file:')
    
    fileName = FileUtils.selectSaveFile()
    
    print()
    
    if fileName == None: 
        print('No file selected. Exiting program...')
        os._exit(0)
        
    else: 
        
        openFile = open(fileName, 'w')
        
        for score in studentScores:
            
            openFile.write(score + "\n")
            
        print('Saving...')
        print()            
        
        openFile.close()
        
    print('***********************************')
    print()
        
#---------------- Part 2 -------------------

    print('PART TWO')
    print()
        
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
    
#============================================

main()