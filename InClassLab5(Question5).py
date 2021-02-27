numStudents = int(input('Enter the number of students who took the quizzes: '))

for student in range(1, numStudents+1):
    studentName = input('Enter the name of student ' + str(student) + ': ')
    totalScore = 0
    
    for quiz in range(1,4):
        score = int(input('Enter score of Quiz ' + str(quiz) + ': '))
        totalScore += score
    average = totalScore / quiz
    print('Name: ', studentName)
    print('Average: ', format(average, "1.2f"))
    print()
                
print('That is all the students.')