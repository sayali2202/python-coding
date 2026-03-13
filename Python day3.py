# #Day3
# #1.
# #larger number
# n1=int(input("Enter number1: "))
# n2=int(input("Enter number2: "))
# n3=int(input("Enter number3: "))
# if n1>n2:
#     if n1>n3:
#         print("n1 is larger.")
#     else:
#         print("n3 is larger.")
# else:
#     if n2>n3:
#         print("n2 is larger.")
#     else:
#         print("n3 is larger.")


#2.
# #to accept percentage and print the grade according to the percentage.
# percentage = float(input("Enter the percentage: "))
# if percentage>=90:
#     print("Grade A")
# elif percentage>=80 and percentage<90:
#     print("Grade B")
# elif percentage>=60 and percentage<80:
#     print("Grade C")
# else:
#     print("Fail")

#3.
# #dictionary datatype : syntax = {key:value}, duplicate keys are not allowed, values can be duplicate,growable in nature, it is mutable, it is unordered.
# mydict={
#     "name":"Vidhi",
#     "age":19,
#     "profession":"student",
#     "studentId":12345
# }
# print(mydict)
# print(type(mydict))

# mydict={
#     101:"Vidhi",
#     102:"Riya",
#     "103":"Sonal",
#     "104":"Pooja",
#     101:"Ashish",
#     104:"Ashish"
# }
# print(mydict)

# #when again 101 is added with new value, the old value are replaced by the new value because duplicate keys are not allowed in dictionary. 
# #for 104, firstly for Pooja it's a string and for Ashish its an integer, so it is not a duplicate key because of different data types.

# #to print a perticular key value.
# a = mydict[102]
# print(a)

# #to update a value of a key.
# mydict[102]="Riya Sharma"
# print(mydict)

# #print all the keys, here x automatically points out at the keys.
# for x in mydict:
#     print(x)

# #to print only the values, here x automatically points out at the keys and mydict[x] gives the value of that key.
# for x in mydict.values():
#     print(x)

# #to print both keys and values, here x automatically points out at the keys and mydict[x] gives the value of that key.
# for x,y in mydict.items():
#     print(x,y)

# #to add new key and value in the dictionary.
# mydict["Mobile_no"]=1234567890
# print(mydict)

# #to remove 
# mydict.pop(101)
# print(mydict)

# #4.
# #string
# name = "vidhiharde"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

# #5.
# #finding index
# s="Helpcode is the best platform for practicing programming."
# print(s.find("Helpcode"))
# print(s.find("Python")) #when there is no value to find, it returns -1.
# print(s.find("programming"))

# #6.
# #joining strings
# s = "Vidhi", "Riya", "Sonal", "Pooja"
# m = " --> ".join(s)
# print(m)

# #7.
# #changing casees
# s="Helpcode is the best platform for practicing programming."
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# #8.
# #dot format function
# print('Subjects Marks:')
# phy=50
# chem=60
# maths=70
# #three ways to print the marks of subjects using dot format function.
# print("Physics={} chemistry={} maths={}".format(phy,chem,maths))
# print("Physics={0} chemistry={1} maths={2}".format(phy,chem,maths))
# print("Physics={x} chemistry={y} maths={z}".format(x=phy, y=chem, z=maths))
# total=phy+chem+maths
# print("Total marks=",f"{total}")
# print("Roll no.","7".zfill(4))

# #9.
# #some more functions : gives boolean values.
# print("VidhiHarde0121".isalnum())
# print("VidhiHarde".isalpha())
# print("0121".isdigit())
# print("sdsdsdsdsd".islower())
# print(" ".islower())
# print("VIDHIH".isupper())
# print("My name is Vidhi".istitle())
# print(" ".istitle())
# print(" ".isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

# #10.
# #bodmas
# a=50
# b=30
# c=20
# d=10

# print((a+b)*c/d) #first c/d is calculated then b*(c/d) and then a+(b*(c/d)) answer 160
# print((a-b)*(c/d)) #first (a+b) is calculated then (a+b)*c and then ((a+b)*c)/d answer 40
# print(a+(b*c)/d) #first b*c is calculated then (b*c)/d and then a+((b*c)/d) answer 110

# #11.
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x !=z)

# #12.
# #to check if a character is vowel or consonent and to count the number of vowels and consonents in a string.
# name = "VidhiHarde"
# consonent=0
# vowel=0

# for i in name:
#     print(i) #i=0

#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         vowel = vowel+1
#     else:
#         consonent= consonent+1

# print("Number of vowels=", vowel)
# print("Number of consonents=", consonent)