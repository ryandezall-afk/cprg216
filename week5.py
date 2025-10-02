'''
REview of if statement
'''
age=18
if age >= 18:
    print ("You are eligible to vote")
else:
    print ("You are not eligible to vote")

# Now while loop
'''
- while : mandantory
- condition true or false : madnatory
- the colon : mandantory
- one or more statements (Indented)
'''
#True all the time

age = 19
is_adult = age >= 18
while is_adult:
    print("The user is adult")
    age = 17
    is_adult = age >= 18

# code to print numbers from 1 to 10

'''i = 1
while i <=10:
    print(i)
    i = i + 1  # i += 1'''

# print number 16 to 55
number = 16
while number <= 55:
    print(number)
    number += 1

i = 10
while i >= 1:
    print(i)
    i -= 1