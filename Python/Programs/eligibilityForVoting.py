name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if(age < 18):
    print(name,"is not eligible for voting")
else:
    print(name,"is eligible for voting")