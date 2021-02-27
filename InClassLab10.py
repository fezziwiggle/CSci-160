'''
Maezy Haldeman: maezy.haldeman@und.edu
Computer Science 1 (Online)
In Class Lab 10
ID#: 1325352

This program takes the text file 'inClassLab10(English to Latin).txt' and turns its contents 
into a dictionary with English words as the keys and their Latin equivalents as the values.
The program then asks the user to enter an English word and, if that word is in the dictionary,
returns its Latin translation.

'''

import FileUtils
import os

#==========================================

def fillDictFromFile(fileName):
    
    fileDict = {}
    
    if fileName == None: 
        
        print('No file selected. Exiting program...')
        os._exit(0)
        
    if os.path.isfile(fileName) == False: 
        print ("Entered file doesn't exist. Exiting program...")
        os._exit(0)
      
    else:    
    
        openFile = open(fileName, 'r')
        
        for line in openFile:
            
            (eng, lat) = line.split(':')
            fileDict[eng] = lat.strip()
            
        openFile.close()
    
    return fileDict    

#--------------------------------------------------

def isWordInDict(theDict, userKey):
    
    isInDict = False
    
    if userKey in theDict:
        isInDict = True
        
    else:
        isInDict = False
        
    return isInDict
    
#--------------------------------------------------

def findWordInDict(theDict, userKey):
    
    while userKey != '':
        
        isInDict = isWordInDict(theDict, userKey)        
        
        if isInDict == True:
        
            print('Latin:', theDict[userKey])
            print()
            userKey = input('Enter a number one through ten in English: ')
            print()
            
        else:
            
            print('That word is not in the dictionary.')
            print()
            userKey = input('Enter a number one through ten in English: ')
            print()
        
    if userKey == '':
        print('Exiting program...')

#**************************************************

def main():
    
    print('Starting program...')
    print()
    
    print("Select data file for reading: ")
    fileName = FileUtils.selectOpenFile()
    print()
    
    theDict = fillDictFromFile(fileName)
    
    userKey = input('Enter a number one through ten in English (press Enter to quit): ')
    print()
    
    findWordInDict(theDict, userKey)    
    
#===========================================

main()