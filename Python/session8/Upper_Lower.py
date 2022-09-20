def countofchar(string):
    dict = {"upper":0, "lower":0}
    for i in string:
        if i.isupper():
            dict["upper"]+=1
        elif i.islower():
            dict["lower"]+=1
        else:
            pass
    print("Given String:",string)
    print("UpperCase:",dict["upper"])
    print("LowerCase:",dict["lower"])

countofchar("Hello Hacker")