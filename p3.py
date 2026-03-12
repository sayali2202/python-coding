#wap to accept five different value in 5 different var and check max value and print by using "simple if statement"
a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
c = float(input("Enter the third value: "))
d = float(input("Enter the fourth value: "))
e = float(input("Enter the fifth value: "))
max_value = a
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
if d > max_value:
    max_value = d
if e > max_value:
    max_value = e
print("The maximum value is:", max_value)


#using if-elif-else statement
a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
c = float(input("Enter the third value: "))
d = float(input("Enter the fourth value: "))
e = float(input("Enter the fifth value: "))
if a >= b and a >= c and a >= d and a >= e:
    max_value = a
elif b >= a and b >= c and b >= d and b >= e:
    max_value = b
elif c >= a and c >= b and c >= d and c >= e:
    max_value = c
elif d >= a and d >= b and d >= c and d >= e:
    max_value = d
else:
    max_value = e
print("The maximum value is:", max_value)   




#same program minumun value 
n1 = float(input("Enter the first value: "))
n2 = float(input("Enter the second value: "))
n3 = float(input("Enter the third value: "))
if(n1
   <=n2 and n1<=n3):
    min_value = n1
elif(n2<=n1 and n2<=n3):
    min_value = n2
else:
    min_value = n3
print("The minimum value is:", min_value)


#wap to accept tp accept percentage and if per is greater than 90 grade is A, if per greater than 80 grade b, if per greater than 70 grade c, if per greater than 60 grade d, if per greater than 50 grade e, otherwise grade is f
percentage = float(input("Enter the percentage: "))
if percentage > 90:
    grade = 'A' 
elif percentage > 80:
    grade = 'B'
elif percentage > 70:
    grade = 'C'
elif percentage > 60:
    grade = 'D'
elif percentage > 50:
    grade = 'E'
else:
    grade = 'F'
print("The grade is:", grade)