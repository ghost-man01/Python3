x = 10
y = 4

print("x:",x)
print("y:",y)

if(x & y):  # Number is converting into binary then bitwise-AND operator works with operands 
    print("Bitwise-OR resulting True") #If it's bitwise-AND is resulting 1
else:
    print("Bitwise-OR resulting False") # If bitwise-AND resulting 0

y = 0
if (x | y):
    print("It's for True from bitwise-OR")
else:
    print("It's for False from bitwise-OR")

if (x ^ y):
    print("Bitwise-XOR resulting True")
else:
    print("Bitwise-XOR resulting False")

x <<= 2
print("Left Sift of x by 2:", x)

y >>= 2
print("Right Shift of y by 2:", y)


