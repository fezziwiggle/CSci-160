def input_numbers():
    x = 1
    
    numbers = []
    x = int(input('Enter the first number: '))
    while x != 0:
        
        numbers.append(x)
        x = int(input('Enter the next number: '))
    
    print( numbers)
    

input_numbers()
