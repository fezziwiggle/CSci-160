'''
160 Computer Science 1: Online
Lab 6 Part 1
Maezy Haldeman: maezy.haldeman@und.edu
ID#: 1325352

Lab 6 Part 1 asks the user to open/create a file for writing. If the user selects/creates a file, 
the program asks for a test score between 0 and 100 until the user enters -1 (or any number outside of [0, 100]).
If the user doesn't select a file, the program exists right away.
'''

import FileUtils
import os

print("Select data file: ")

fileName = FileUtils.selectSaveFile()
print()
#fileName = 'scores1.txt'

if fileName == None: #exits program if no file was selected
    
    print('No file selected. Exiting program...')
    os._exit(0)
    
else: #continues on if file was selected
    
    openFile = open(fileName, 'w')
    
    print("Enter '-1' at any time to quit.")
    
    print('Enter test scores between 0 and 100 below.')
    
    testScore = int(input('Enter a test score: '))
    
    while 0 <= testScore <= 100: #as long as testScore is within [0,100], program will write testScore to file on newline
        openFile.write(str(testScore) + '\n')
        testScore = int(input('Enter a test score: '))
    
print()
        

print('Writing to', fileName, 'completed. Exiting program...')
openFile.close()







