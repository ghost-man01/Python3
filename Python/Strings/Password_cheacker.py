name = str(input("Enter your name: "))
if name.islower() == True:
    name = name.capitalize()
    print("Name:",name)
else:
    print("Name should only contain characters")
id = int(input("Enter your id: "))
print("Id:",id)

password = str(input("Enter your password: "))
if len(password) >= 8:
    if password.isalnum() == True:
        if password.find(name) == -1:
            if password.startswith(name.lower() or id) != name:
                password = password.replace(password,'*'*len(password))
                print("Password:",password)
            else:
                print("Your password should not STARTS with NAME")
        else:
            print("Your password should not contain the NAME")
    else:
        print("This is Hackable password")

else:
    print("Your password should have minimum length of 8 characters")