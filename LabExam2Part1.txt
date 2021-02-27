'''
Maezy Haldeman: maezy.haldeman@und.edu
CS160: Computer Science 1
Lab Exam 2 Part 1
ID#: 1325352

This program asks the user for the number of students in a class,
then requests a score for each student. The program then asks the user
to select a file, and then saves the scores to that file.

'''

import FileUtils
import os

#==================================

def main():
    
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
    
#==================================
    
main()