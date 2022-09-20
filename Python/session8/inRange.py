def Range(num):
    first = int(input("Enter first:"))
    last = int(input("Enter last:"))
    if num in range(first, last):
        print("Yes")
    else:
        print("NO")

number = int(input("Enter number: "))
Range(number)