#wap a program for indexing and slicing are not possible in dictionary{key}
mydict = {"name": "Alice", "age": 30, "city": "New York"}
print(mydict["name"])  # Accessing value by key
print(mydict.get("age"))  # Another way to access value by key
print(type(mydict))

mydict ={
    101: "Alice",
    102: "Bob",
    "103": "Charlie",
    "104" : "David",
    101: "Eve"  ,
    104:"ashish",
}
print(mydict) 
 # Output: Eve (the value of key 101

a= mydict[101]
print(a) # Output: Eve (the value of key 101)

#we will ewplace old value by new value
mydict[101] = "Frank"
print(mydict) # Output: Frank (the value of key 101 is updated to Frank)

#only print key X=0,1
for X in mydict:
 print(X) # Output: 101, 102, "103", "104" (the keys of the dictionary)

#only print values
for X in mydict.values():
 print(X) # Output: Frank, Bob, Charlie, ashish (the values of the dictionary)

#only print key and value
for X,y in mydict.items():
 print(X, y) # Output: (101, 'Frank'), (102, 'Bob'), ('103', 'Charlie'), ('104', 'ashish') (the key-value pairs of the dictionary)

 # if i have to ad new key and value pair  in my dictionary
mydict[105] = "Grace"
print(mydict) # Output: {101: 'Frank', 102: 'Bob', '103': 'Charlie', '104': 'ashish', 105: 'Grace'} (the new key-value pair is added to the dictionary)
mydict["mobile number"] = 1234567890
print(mydict) # Output: {101: 'Frank', 102: 'Bob', '103': 'Charlie', '104': 'ashish', 105: 'Grace', 'mobile number': 1234567890} (the new key-value pair is added to the dictionary)


#remove key and value pair from dictionary
mydict.pop(102) # Output: Bob (the value of key 102 is removed from the dictionary)
print(mydict) # Output: {101: 'Frank', '103': 'Charlie', '104': 'ashish', 105: 'Grace', 'mobile number': 1234567890} (the key-value pair with key 102 is removed from the dictionary)
name = "theayung"
#indexing = 012345678910
print(name[0]) 
print(name[1])
print(name[-1])
print(name[0:5])
print(name[1:])
print(name[:5])
print(name[1:8:2])
print(name[::-1])

#code for find method

s ="help4cose is a best platform for practicing programming"
print(s.find("help4code"))
print(s.find("best"))
print(s.find("python"))


#print
s = "sayali","twinkle","snehal"
m = '|'.join(s)
print(m) # Output: sayali|twinkle|snehal (the elements of
print(s) # Output: ('sayali', 'twinkle', 'snehal')

s =" python is a high level programming language"
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())

#value store can write in different syntaxs
print('stubjects marks:')
phy = 60
chme =70
math = 80
print("physics ={}, chemistry ={}, math ={}".format(phy, chme, math))
print("physics = {0}, chemistry = {1}, math = {2}".format(phy, chme, math))
print("physics={x}, chemistry={y}, math={z}".format(x=phy, y=chme, z=math))
total = phy + chme + math
print("total marks = {}".format(total))
print("total marks",f"{total}")
print("roll number = ","7".zfill(4))


#print string method
print('prashantjha777'.isalnum())
print('prashantjha'.isalpha())
print('123456'.isdigit())
print(' '.isspace())
print('sdsdsdsd'.islower())
print('SDSDSDSD'.isupper())
print(''.islower())
print(' my name is prasant'.istitle())
print(''.istitle())
print(''.isspace())
print("hello".startswith("he"))
print("hello".endswith("lo"))    


#bodmas
a=50
b=30
c=20
d=10
print((a+b)*c/d) # Output: 100.0 (the result of the expression following the BODMAS rule)
print((a-b)*(c/d)) # Output: 100.0 (the result of the expression following the BODMAS rule)
print(a+(b*c)/d) # Output: 110.0 (the result of the expression following the BODMAS rule)


x=['a','b','c']
y=['a','b','c']
z=[1,2,3,4]
print(x==y) # Output: True (the lists x and y have the same elements in the same order)
print(x==z)
print(x !=z)

#count vowels and consonants 
name = "prashant"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for i in name:
    if i in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

#remove duplicate characters in string name = "prashant"
name = "prashant"
unique_chars = ""
for i in name:
    if i not in unique_chars:
        unique_chars += i
print("String with duplicate characters removed:", unique_chars)