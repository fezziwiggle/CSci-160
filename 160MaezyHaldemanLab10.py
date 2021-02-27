'''
Maezy Haldeman: maezy.haldeman@und.edu
Computer Science 1 (Online)
In Class Lab 10
ID#: 1325352

This program asks the user for an existing text file and prints a table of the number of ocurrences for
each character. The program then prints the least ocurring characters and most ocurring characters.

'''

import FileUtils
import os

#======================================= 

def readFileLines(fileName): #reads the user selected file and turns its lines into a list
    
    if fileName == None: 
        
        print('No file selected. Exiting program...')
        os._exit(0)
                                               
    if os.path.isfile(fileName) == False: 
        print ("Entered file doesn't exist. Exiting program...")
        os._exit(0)
      
    else:   
            
        openFile = open(fileName, 'r')
        
        fileLines = openFile.readlines()
        
        openFile.close()
    
    return fileLines

#----------------------------------------- 

def fillDictFromFileLines(fileLines): 
    
    fileDict = {}
        
    for element in fileLines: #accesses every element in the list
    
        for character in element: #accesses every character in every element
            
            lowerCharacter = character.lower() #makes every character the same case
            
            if lowerCharacter in 'abcdefghijklmnopqrstuvwxyz': #if the character is a letter, create or update its dictionary entry
                
                if character in fileDict: #Increment count of character by 1 

                    fileDict[lowerCharacter] = fileDict[lowerCharacter] + 1
    
                else: #Add the character to dictionary with count 1 
                        
                    fileDict[lowerCharacter] = 1     
                    
    return fileDict

#---------------------------------------

def findLeastOcurringCharacter(characterDict): #takes the dictionary of characters and finds and prints the characters ocurring the least
    
    firstLeastValue = min(characterDict.values()) #finds the minimum value in the dict
    allLeastValues = [key for key in characterDict if characterDict[key] == firstLeastValue] #retrieves all the keys with that minimum value
    
    print('Letter(s) with the least ocurrences: ocurrences =', firstLeastValue)       
    
    for element in allLeastValues:
        
        print(element)
        
    return ''
    
#---------------------------------------

def findMostOcurringCharacter(characterDict): #takes the dictionary of characters and finds and prints the characters ocurring the most
    
    firstMostValue = max(characterDict.values()) #finds the maximum value in the dict
    allMostValues = [key for key in characterDict if characterDict[key] == firstMostValue] #retrieves all the keys with that maximum value 
    
    print('Letter(s) with the most ocurrences: ocurrences =', firstMostValue)           
    
    for element in allMostValues:
        
        print(element)   
        
    return ''
        
#---------------------------------------

def printCharacterDict(characterDict):
    
    print(format('Letter:', '1s'), format('Count:', '>7s'))
    
    for character in characterDict:
        
        print(format(character, '>4s'), format(characterDict[character], '8d'))
        
        
#***************************************

def main():

    print("Select data file for reading: ")
    fileName = FileUtils.selectOpenFile()
    print()
    
    linesFromFile = readFileLines(fileName)
    characterDict = fillDictFromFileLines(linesFromFile)
    characterValues = []
    
    for value in characterDict.values():
        characterValues.append(value)
        
    characterValues.sort()
      
    print('----------------')
    printCharacterDict(characterDict)
    print('----------------')
    
    print()
    leastOcurringCharacters = findLeastOcurringCharacter(characterDict)
    print(leastOcurringCharacters)
    
    mostOcurringCharacters = findMostOcurringCharacter(characterDict)
    print(mostOcurringCharacters)        
    
#***************************************

#=======================================

main()