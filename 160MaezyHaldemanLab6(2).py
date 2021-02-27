'''
160 Computer Science 1: Online
Lab 6 Part 2
Maezy Haldeman: maezy.haldeman@und.edu
ID#: 1325352

Lab 6 Part 2 asks the user to select a file to read (can be file written by Lab 6 Part 1 program). 
The program then iterates through each line in the file and performs logic tests to check for the minimum value,
maximum value, average value, total number of values, total number of values greater than or equal to 70, 
the total number of values less tha 70, the value closest to 70, and the value closes to 70 without being greater than 70.

'''

import FileUtils
import os


print("Select data file: ")
fileName = FileUtils.selectSaveFile()
print()
#fileName = 'scores1.txt'


#initializing variables
minValue = 9999999
maxValue = 0
avgValue = 0
numValues = 0
big70Values = 0
small70Values = 0
close70 = 0
upTo70 = 0
totalValues = 0

if fileName == None: #exits program if no file was selected
    
    print('No file selected. Exiting program...')
    os._exit(0)
    
if os.path.isfile(fileName) == False: #the selected/entered file does not exist
    print ("Entered file doesn't exist")
    os._exit(0)
  
else: #continues on if file was selected
    
    openFile = open(fileName, 'r')
    
    for line in openFile:
        
        line = line.strip() #remove the CR at the end of the line
        
        totalValues += int(line) 
        
        #minimum value
        if numValues == 0:
            minValue = int(line)
        elif int(line) < int(minValue): 
            minValue = int(line) 
            
        #maximum value        
        if int(line) > int(maxValue): 
            maxValue = int(line)        
            
        #number of values
        numValues += 1
        
        #number of values greater than or equal to 70
        if int(line) >= 70:
            big70Values += 1
        
        #number of values less than 70
        if int(line) < 70:
            small70Values += 1
        
        #the value closest to 70, can be 70
        if numValues == 0:
            close70 = int(line)
        elif abs(70 - (int(line))) < abs(70 - close70):
            close70 = int(line)
        
        #the value closest to 70, not greater than 70
        if numValues == 0 and int(line) < 70:
            upTo70 = int(line)
        elif abs(70 - (int(line))) < abs(70 - upTo70) and int(line) < 70:
            upTo70 = int(line)        
         
#average value
avgValue = format((totalValues / numValues), "1.3f")

print('Minimum value is:', minValue)
print('Maximum value is:', maxValue)
print('Average value is:', avgValue)
print('Number of values is:', numValues)
print('The number of values greater than or equal to 70 is:', big70Values)
print('The number of values less than 70 is:', small70Values)
print('The value closest to 70 is:', close70)
print('The value closest to 70 that is not greater than 70 is:', upTo70)

print()

print('Reading', fileName, 'completed. Exiting program...')    
openFile.close()
    
    