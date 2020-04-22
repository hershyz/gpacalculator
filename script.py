classes = []
grades = []

def findGPA(_grade):
    grade = int(_grade)
    if (grade >= 90):
        return 4.0
    if (grade >= 80):
        return 3.0
    if (grade >= 70):
        return 2.0
    if (grade >= 60):
        return 1.0
    else:
        return 0

def showSummary():

    gpaTotal = 0
    print("-------------------------")

    i = 0
    while (i < len(grades)):
        currentGPA = findGPA(grades[i])
        gpaTotal = gpaTotal + currentGPA
        print(classes[i] + ": " + str(currentGPA))
        i += 1
    
    cumalative = gpaTotal / len(grades)
    print("Cumalative: " + str(cumalative))

def collect():
    classTotal = int(input("Enter total number of classes: "))
    print("-------------------------")
    x = 0
    while (x < classTotal):
        classPosition = x + 1
        className = input("Class " + str(classPosition) + ": ")
        classes.append(className)
        x += 1
    
    print("-------------------------")
    
    y = 0
    while (y < len(classes)):
        grade = input(classes[y] + " grade: ")
        grades.append(grade)
        y += 1

    showSummary()

collect()
