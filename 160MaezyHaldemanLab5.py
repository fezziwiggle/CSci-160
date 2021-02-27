course = input('Enter a course: ')

attCredits = 0
attCourses = 0

passCredits = 0
passCourses = 0

honorPoints = 0

GPA = 0.0

if len(course) != 0:
    
    while len(course) != 0:
    
        #number of credits a course is
        courseCredits = int(input('Enter the number of credits: '))
        attCredits += courseCredits #adds current course credits to total attempted credits
        
        
        courseGrade = input('Enter your grade: ') #grade for current course
        if courseGrade == 'A' or courseGrade == 'a': #number versions of letter grades
            coursePoints = 4
        elif courseGrade == 'B' or courseGrade == 'b':
            coursePoints = 3
        elif courseGrade == 'C' or courseGrade == 'c':
            coursePoints = 2
        elif courseGrade == 'D' or courseGrade == 'd':
            coursePoints = 1
        else:
            coursePoints = 0
        
        honorPoints = honorPoints + (courseCredits * coursePoints) #calculates the number of honor points for the current course
        
        print()
        
        if courseGrade != 'F' and courseGrade != 'f': #if passing grade, add one to passed courses and add the current course credits to passed credits
            passCourses += 1
            passCredits += courseCredits
                    
        attCourses += 1
        
        course = input('Enter the next course: ')
    
    
else:
    print('No courses were entered.')
    print('GPA:', GPA)


if attCredits > 0:
    GPA = honorPoints / attCredits
else:
    GPA = 0.0

print()

print('GPA: ', end='') 
print(format((format(GPA, '1.3f')), '>19s'))
    
print('Credits attemtped:', end='')
print(format(attCredits, '>6d'))

print('Credits passed:', end='')
print(format(passCredits, '>9d'))

print('Courses attempted:', end='')
print(format(attCourses, '>6d'))

print('Courses passed:', end='')
print(format(passCourses, '>9d'))
