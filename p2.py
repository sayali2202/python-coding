#wap to accept days and check the working day or not
day=input("Enter the day:")
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Working day")
elif day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Invalid day")


#write a program to accept 3 paper marks and calculate total,percentage and if percentage is greater than 60 then he/she is eligible for placement otherwise not
marks = []
for i in range(3):
    mark = float(input("Enter the mark for paper {}: ".format(i+1)))
    marks.append(mark)

total = sum(marks)
percentage = total / 3

print("Total marks:", total)
print("Percentage:", percentage)

if percentage > 60:
    print("Eligible for placement")
else:
    print("Not eligible for placement")