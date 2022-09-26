furniture = {"Sofa set":20000, "Dining table":8500, "T.V. Stand":4599, "Cupboard":13920}

user = input("Enter your name: ")
name = input("Enter Furniture name: ")

if name in furniture:
    quan = int(input("Enter Quantity of set: "))
    if quan > 0:
        print("Thank You!", user, "for using our service")
        print("You've to pay Bill:",furniture[name]*quan)
    else:
        print(user, "you entered 0 or less than 0")
        print("Don't be smart to know Price of Furniture")
        print("Bill: 0")
else:
    print("Sorry! This item is not present in our Store")
    print("Thank You! for using our Service")


