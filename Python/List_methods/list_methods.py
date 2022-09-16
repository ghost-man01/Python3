#.append(x) --> Add element x to end of list
#.sort() --> sort(order) the list A comparsion function may be passed as a parameter
#.reverse() -->  reverse of list
#.index(x) --> returns index of first occurence of x
#.insert(i,x) --> insert x into list at index i.
#.count(x) ---> returns the number of occurences of x in list
#.remove(x) ---> deletes the first occurence of x in list 
#.pop(x)  --- Deletes the ith element of the list and returns its value


list = []
list.append("hacker")
print("Appending:", list)

let = [1,2,5,4,2]
let.sort()
print("Sorting:",let)

low = [1,2,3,4,5,6]
low.reverse()
print("Reverse:",low)

new = [1,3,4,5,8]
print("index:",new.index(5))

arr = [1,34,33]
arr.insert(4,3)
print("insert:",arr)

never = [1,1,2,3,3,34,3,5,3]
print("count:",never.count(3))

hello = [2,3,5,32,34,3,9]
print("remove:",hello.remove(3))

nothing = [3, 4, 5, 2, 4, 5]
print("pop:",nothing.pop(4))
