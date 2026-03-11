# mylist store values and print the values in variouos ways

mylist = [1, 2, 3, 4, 5]

# print the values in the list
print(mylist)

# print the values in the list using a for loop
for i in mylist:
    print(i)

#take input list of names integers and floats and print the values in the list
mylist2 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = input("Enter the element: ")
    mylist2.append(element)
print(mylist2)

#also print values separately
for i in mylist2:
    print(i)
    
#example
mylist=["inaas","saara","sayali","siddhant", "Viraj", 77, "daphne", 60.52, "lara"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:5])

mylist=["inaas","saara","sayali","siddhant", "Viraj", 77, "daphne", 60.52, "lara"]
mylist.append("twinkle")
print(mylist)
mylist.insert(2, "twinkle")
print(mylist)
mylist.remove("twinkle")
print(mylist)
newlist = mylist.copy()
print(newlist)
print(mylist.count("twinkle"))
mylist.clear()
print(mylist)

#sorting example
mylist = [5, 2, 9, 1, 5, 6]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

#default sorting is in ascending order and reverse sorting is in descending order
#sorting in alphabetical order
mylist = ["banana", "apple", "cherry", "date"]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)


#example of list comprehension
squares = [x**2 for x in range(10)]
print(squares)

mylist=[['inaas','saara'],['85.56'],[440022, "yyy"]]
print("multidimensional list: ")
print(mylist)
#print(mylist[row][col])
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])

mylist=["inaas","saara","sayali","siddhant", "Viraj", 77, "daphne", 60.52, "lara"]
mylist.insert(1,"kavinsky")
print(mylist)
mylist.remove("siddhant")
print(mylist)
newlist=mylist.copy()
print(mylist)
print(newlist)

mylist=["inaas","saara","sayali","siddhant", "Viraj", 77, "daphne", 60.52, "lara"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])

list2=[50,25,50,'inaas']
del list2[2]
print(list2)

list3=[50,25,50,'saara']
list3.clear()
print(list3)

name="inaas"
print(name)
myname=list(name)
print(myname)

mylist=[44,22,33,55,66,77]
mylist.sort()
print(mylist)

mylist=[44,22,33,55,66,77]
mylist.sort(reverse=True)
print(mylist)

math=10
print(id(math))

name="inaas"
print("2" in name)
print("2" not in name)

for i in range(2,6):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(5,0,-1):
    print(i*2)

for i in range(1,11):
    print(i*2," ",i*3)

