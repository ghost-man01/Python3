nameOfStudent = str(input("Enter your Name: "))
marksOfStudent = int(input("Enter your Marks: "))
stringofMarks = str(marksOfStudent)

if (marksOfStudent > 85 and marksOfStudent <= 100):
    print(nameOfStudent,stringofMarks,"A")
elif (marksOfStudent > 60 and marksOfStudent <= 85):
    print(nameOfStudent,stringofMarks,"B+")
elif (marksOfStudent > 40 and marksOfStudent <= 60):
    print(nameOfStudent,stringofMarks,"B")
elif (marksOfStudent > 30 and marksOfStudent <= 40):
    print(nameOfStudent,stringofMarks,"C")
else:
    print(nameOfStudent,stringofMarks,"Fail")
