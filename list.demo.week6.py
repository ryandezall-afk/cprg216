'''x = 2 #cpu will allocate 4 bytes in ,emore, give the name x to that, value is 2

data = [3, 4, 5]
data[2]
print(data)
print(data[2])

days = []
print(days)
#print(days[0])
#this is out of range will not print

#print(data[5])
#this is out of range and will not print

week = ['sun', 'mon', 'tues', 'wed', 'thur', 'fri', 'sat']

#print(week[8])
#will not work out of range
print(week[1])'''

data=[1,2,3,4,5]
week = ['sun', 'mon', 'tues', 'wed', 'thur', 'fri', 'sat']

for item in data:
    square = item**2
    print(item, square)

for day in week:
    print(day)
l = len(week)
print(l)
print(len(week))

for day in week:
    print(l, day)

range(7)
print(list(range(len(week))))

for i in range(len(week)):
    print(week[i],end='\t')

