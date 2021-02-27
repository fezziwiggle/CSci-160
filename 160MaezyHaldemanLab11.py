'''
Maezy Haldeman: maezy.haldeman@und.edu
CS160: Computer Science 1
Weekly Lab 11
ID#: 1325352

This program displays a menu of options for reading an manipulation information from
a .txt file of names and birthdays. The user can read a file of birthdays, 
make a dictionary with the birthdays as keys and names as values,
add new names to the dictionary, search the dictionary by date,
display all birthdays from the file, and write the updated dictionary
back to the selected file.

'''

import FileUtils
import os

#==========================================

def printMenuChoices(): #displays menu for user to choose from
    
    print('Select a menu option:')
    print('   1. Open a data file')
    print('   2. Add a new name')
    print('   3. Search by date')
    print('   4. Display all birthdays for the month')
    print('   5. Exit program')
    print()
    
#------------------------------------------

def showMenu(): #calls printMenuChoices and saves the user's choice
    
    printMenuChoices()
    menuChoice = int(input('Your choice: '))
    
    while menuChoice < 1 or menuChoice > 5:
        
        print('Please enter a valid menu option (1-5)')
        print()
        menuChoice = int(input('Your choice: '))
        
    return menuChoice

#------------------------------------------

def getBirthdayDict(fileName): #choice 1 - opens file and saves names and birthdays to a dictionary
    
    if fileName == None: 
        
        print()
        print('No file selected. Exiting program...')
        os._exit(0)
                                               
    if os.path.isfile(fileName) == False: 
        
        print()
        print ("Entered file doesn't exist. Exiting program...")
        os._exit(0)
      
    else:   
        
        birthdayDict = {}
        openFile = open(fileName, "r")
        
        for line in openFile:
            
            line = line.strip()
            (name, birthday) = line.split(":")
            birthdayDict[birthday] = name
            
        openFile.close()
                
        return birthdayDict        

#------------------------------------------

def addToDict(birthdayDict): #choice 2 - adds a new name and birthday pair to the dictionary
    
    nameToAdd = input('Name to add: ')
    dateToAdd = input('Birthday for ' + nameToAdd + ': ')
    
    if dateToAdd in birthdayDict:
        
        dateToAdd = input('That date is taken. Please enter another date: ')
        
    if dateToAdd not in birthdayDict:
        
        birthdayDict[dateToAdd] = nameToAdd
        print(nameToAdd, 'has been added to the birthday list.')

#------------------------------------------

def searchDictByDate(birthdayDict): #choice 3 - searches the dictioary of birthdays by date and displays the respective name
    
    userDate = input('Enter a date (or 0 to quit): ')
    
    while userDate != '0':
        
        if userDate in birthdayDict:
            
            print('Birthday for ', userDate, ': ', birthdayDict[userDate], sep='')
            print()
            userDate = input('Enter a date (or 0 to quit): ')            
            
        else:
            
            print('There are no birthdays for', userDate)
            print()
            userDate = input('Enter a date (or 0 to quit): ')        
            
#------------------------------------------

def displayDictBirthdays(birthdayDict): #choice 4 - displays all birthdays in the dictionary from the .txt file
    
    for date in birthdayDict:
        
        print(format(birthdayDict[date], "10s"), format(date, ">2s"))

#------------------------------------------

def saveBirthdayDict(fileName, birthdayDict): # choice 5 - saves all changes in the dict back into the user selected file
    
    openFile = open(fileName, "w")    
    
    for date in birthdayDict:
                
        openFile.write (birthdayDict[date] + ":" + date + "\n")       
        
    openFile.close()
    
#------------------------------------------


#****************************************** #main function

def main():
    
    print()
    userChoice = showMenu()
    
    while userChoice != 5:
        
        if userChoice == 1: #open file and return a dictionary with the info

            fileName = FileUtils.selectOpenFile()
            birthdayDict = getBirthdayDict(fileName)
            print()

        elif userChoice == 2: #allow the user to add new name/birthday

            addToDict(birthdayDict)
            print()

        elif userChoice == 3: #ask for a date and display the associated name

            searchDictByDate(birthdayDict)
            print()

        elif userChoice == 4: #display all dates/names for the month

            displayDictBirthdays(birthdayDict)
            print()
            
        userChoice = showMenu()
        print()
   
    if userChoice == 5: #write the dictionary back to the original file 
        
        saveBirthdayDict(fileName, birthdayDict)
        print('Updated ', fileName, '. Exiting program...', sep='')
        os._exit(0)      
    
#******************************************

main()