import FileUtils

#print("Select data file: ")
fileName = input ("Select data file: ")
print()

openFile = open(fileName, 'r')

fileList = openFile.readlines()

strippedList = []

for item in fileList:
    item = item.strip()

#for line in openFile:
    
 #   line = line.strip()

        
#fileList = list(openFile)

print(strippedList)