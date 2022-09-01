nameOfStudent = str(input("Enter your Name: "))
marksOfStudent = int(input("Enter your Marks: "))

if (marksOfStudent > 85 and marksOfStudent <= 100):
    print(nameOfStudent,"A")
elif (marksOfStudent > 60 and marksOfStudent <= 85):
    print(nameOfStudent,"B+")
elif (marksOfStudent > 40 and marksOfStudent <= 60):
    print(nameOfStudent,"B")
elif (marksOfStudent > 30 and marksOfStudent <= 40):
    print(nameOfStudent,"C")
else:
    print("Fail")
