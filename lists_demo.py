#killer means single value

numbers = [1, 2, 3, 4, 5, 6]
week = ['sat, sun, mon, tues, wed, thurs, fri']

print (week)
print (numbers)

#for i in range(0,6):
#    print (i)

for day in week:
    print (day)

for number in numbers:
    square = number **2
    print (square)

gpas = [2,3,4]
gpas.append(3.4)
sum = 0
for gpa in gpas:
    sum += gpa
    print (gpa)