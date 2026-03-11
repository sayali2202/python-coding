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
