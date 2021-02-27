
temp = int(input('Enter a tempurature: '))

if temp != 999:

    #a)
    if temp <= -25:
        print('The tempurature is: extremely cold')
    elif -24 <= temp <= 10:
        print('The tempurature is: cold')
    elif 11 <= temp <= 32:
        print('The tempurature is: warm')
    elif temp >= 33:
        print('The tempurature is: extremely hot')
    
    #b)
    avg = 20
    distance = 0
    
    if temp >= avg:
        distance = temp - avg
    elif temp <= avg:
        distance = avg - temp
    
    print(temp, 'is', distance, 'degrees away from the average tempurature.')
    
    #c)
    
    farenheit = temp * 1.8 + 32
    
    print('The tempurature', temp, 'degrees Celcius is', farenheit, 'degrees Farenheit.')
    
else:
    print("That's too hot. Goodbye!")
    
