x = 4
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(y//y)

# Checking For precidence
c = x*y+y/x-x+y**x
print(c)

# when they have equal precidence

x = 10
y = 20

c = x*y/x*x # Left to right for same precedence
print(c)