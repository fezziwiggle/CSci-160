'''
Maezy Haldeman: maezy.haldeman@und.edu
CS160: Computer Science 1
Final Lab Exam
ID#: 1325352

This program takes the file "food.txt" and fills a dictionary from the file
with the food items as keys and their prices as values. The program then displays a 
menu for the user to choose what to do with the food items in the dictonary. The
program then saves the updated dictionary to "food.txt".

'''

import FileUtils
import os

#===========================================

def printMenuChoices(): #displays menu for user to choose from
    
    print('Select a menu option:')
    print('   1. Add food item')
    print('   2. Print all food items')
    print('   3. Search for a food item')
    print('   4. Take an order')
    print('   5. Search by price')
    print('   6. Exit program')
    print()
    
#-------------------------------------------

def showMenu(): #calls printMenuChoices and saves the user's choice
    
    printMenuChoices()
    menuChoice = int(input('Your choice: '))
    
    while menuChoice < 1 or menuChoice > 6:
        
        print('Please enter a valid menu option (1-6)')
        print()
        menuChoice = int(input('Your choice: '))
        
    return menuChoice

#-------------------------------------------

def fillDictFromFile(fileName): #fills a dictionary from the file with food items as keys and their prices as values
    
    foodDict = {}
    openFile = open(fileName, "r")
    
    for line in openFile:
        
        line = line.strip()
        (item, cost) = line.split(":")
        foodDict[item] = cost
        
    openFile.close()
            
    return foodDict

#-------------------------------------------

def addFoodItem(foodDict): #adds a new food item and price to the foodDict
    
    print()
    foodToAdd = input('Enter a new food item (hit enter to quit): ')
    
    while foodToAdd != '':
        
        priceForFood = input('New item price: ')
        foodDict[foodToAdd] = priceForFood
        
        print()
        foodToAdd = input('Enter a new food item: ')
        
#-------------------------------------------

def printAllFoodItems(foodDict): #prints all key value pairs in the foodDict
    
    print()
    print('Current food items:')
    for item in foodDict:
        
        print(format(item, "20s"), format(foodDict[item], ">2s"))   
        
#-------------------------------------------

def searchForFoodItem(foodDict): #searches the foodDict for the user's food to find
    
    foodToFind = input('Enter item name (hit enter to quit): ')
    
    while foodToFind!= '':
    
        if foodToFind.lower() in foodDict:
        
            print('Cost of ', foodToFind, ': ', foodDict[foodToFind.lower()], sep='')
            print()
            foodToFind = input('Enter item name: ')
        
        else:
            
            print('We do not have', foodToFind)
            print()
            foodToFind = input('Enter item name: ')
        
#-------------------------------------------

def takeAnOrder(foodDict): #takes an order from the user and displays the total items and price of the order from the foodDict
    
    foodOrder = input('Enter food item (hit enter to quit): ')
    totalPrice = 0
    totalItems = 0
    
    while foodOrder != '':
        
        if foodOrder.lower() in foodDict:
        
            foodQuantity = int(input('Quantity: '))
            totalPrice += (foodQuantity * float(foodDict[foodOrder.lower()]))
            totalItems += foodQuantity
            print()
            foodOrder = input('Enter food item: ')
            
        else:
            
            print('That item is not on the menu')
            print()
            foodOrder = input('Enter food item: ')
            
    print()
    print('Food order:')
    print('Total items:', totalItems)
    print('Total price: $', format(totalPrice, "1.2f"), sep='')
        
#-------------------------------------------

def searchByPrice(foodDict): #searches the items in the foodDict by price and displays the items within the user's range
    
    lowerLimit = float(input('Enter lower limit: '))
    upperLimit = float(input('Enter upper limit: '))
    print()
            
    print('Food items in range:')    
    
    for item in foodDict:
        
        if lowerLimit <= float(foodDict[item]) <= upperLimit:
            
            print(format(item, "20s"), format(float(foodDict[item]), "1.2f"))
            
#-------------------------------------------

def saveAndExit(fileName, foodDict): #saves the updated dictionary to the preexisting file
    
    openFile = open(fileName, "w")    
    
    for item in foodDict:
                
        openFile.write (item + ":" + foodDict[item] + "\n")       
        
    openFile.close()    
    

#*******************************************

def main():
    
    fileName = 'food.txt'
    
    foodDict = fillDictFromFile(fileName)

    print()
    userChoice = showMenu()
    
    while userChoice != 6:
    
        if userChoice == 1: #Add food item
    
            addFoodItem(foodDict)
            print()
    
        elif userChoice == 2: #Print all food items
    
            printAllFoodItems(foodDict)
            print()
    
        elif userChoice == 3: #Search for a food item
    
            searchForFoodItem(foodDict)
            print()
    
        elif userChoice == 4: #Take an order
    
            takeAnOrder(foodDict)
            print()
            
        elif userChoice == 5: #Search by price
            
            searchByPrice(foodDict)
            print()            
    
        userChoice = showMenu()
        print()
    
    if userChoice == 6: #Exit program
        
        saveAndExit(fileName, foodDict)
        print('Updated ', fileName, '. Exiting program...', sep='')
        os._exit(0)      

#*******************************************

main()