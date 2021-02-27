'''
160 Computer Science 1: Online
Lab 8 Part 1
Maezy Haldeman: maezy.haldeman@und.edu
ID#: 1325352

'''

import FileUtils
import os

#================= define function for list of user scores ===================

def getUserScores():
    
    score = input('Enter a score, enter -1 to quit: ')
    
    while int(score) >= 0:
        userScores.append(score)
        score = input('Enter the next score: ')
        
    return userScores

#----------------- initialization -------------------

userScores = []

newFile = input('Do you want to create a new file? (yes/no): ')
print()

#------------------ begin loop ------------------

while newFile == 'yes' or newFile == 'Yes':

    fileName = FileUtils.selectSaveFile()
    
    getUserScores()
    print()
    
    if fileName == None: 
        print('No file selected. Exiting program...')
        os._exit(0)
        
    else: 
        
        openFile = open(fileName, 'w')
        
        for score in userScores:
            openFile.write(score + "\n")
            
        print('Saving...')
        print()
            
        openFile.close()
        userScores.clear()
        
        newFile = input('Do you want to create a new file? (yes/no): ')
        print()
            
if newFile == 'no' or newFile == 'No':
    
    print('Exiting program...')
    os._exit(0)
    
#====================================

    
