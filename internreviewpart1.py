import os
path = 'grades.csv'

checkFile = os.path.isfile(path)

if checkFile == True:

    infile = open(path, 'r')
    #class list
    classList = infile.readlines()
    print(classList) 

    #close the file
    infile.close()

else:

    print('file does not exist')

#count the number of grades
gradeLength = len(classList)-1
print(gradeLength)

#create a grade table
gpaList = ('A', 4, 'A-', 3.67, 'B+', 3.33, 'B', 3, 'B-', 2.67, 'C+', 2.33, 'C', 2, 'C-', 1.67, 'D+', 1.33, 'D', 1, 'F', 0)

cumulativeCredits = 0
cumulativeGPA = 0
gradeCount = 1
gpaCheck = 0
processGrade = 0

while processGrade < gradeLength:
    individualClass = classList[gradeCount].split(',')
    #split(',') splits where the commmas are found
    while True:

        if  individualClass[1] == gpaList[gpaCheck]:

            #add to weighted grade
            cumulativeGPA = cumulativeGPA + gpaList[gpaCheck+1] * int(individualClass[0])
            cumulativeCredits = cumulativeCredits + int(individualClass[0])
            break
        gpaCheck = gpaCheck + 2
    
    #reset gpaCheck for next course
    gpaCheck = 0
    gradeCount = gradeCount + 1
    processGrade = processGrade + 1 
    
#calculate the GPA
finalGPA = str(round(cumulativeGPA/cumulativeCredits, 2))
print ('Your Final GPA is: ', finalGPA)
