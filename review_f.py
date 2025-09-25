
'''condition = True

if condition:
    print("Condition is True")
    print("Hello")
    x = 3
    print(x)
elif x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")

else:
    print("Condition is False")

print("Welcome the the party")



I have 5 instructors teaching some courses
Hani CPRG216 -I 2025 Fall
Ashlyn CPRG216 -A 2025 Fall


print("welcome to ")

#combining logical expressions
#and
#or

x =3
y=4
z = 6

condition = (x < y and y < 2 and x < z and instructor in "not found") or 5>10

if not True:
    print("this is true")
if True:
    print("this is false")'''

print("Welcome to the quadratic solver!!")
print("Enter the values for a, b, and c")
a = float(input("Enter a\n"))
b = float(input("Enter B\n"))
c = float(input("Enter c\n"))
x1= None
x2= None

if a == 0:
    x1 = -c/b
    x2 = -c/b
elif 4*a*c <= b**2:
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
else:
    print("There is no possible solution")
print("The value of x1 is:\n", x1, "\nThe value of x2 is:\n", x2)

#edited version
print("Welcome to the quadratic solver!!")
print("Enter the values for a, b, and c")
a = float(input("Enter a\n"))
b = float(input("Enter B\n"))
c = float(input("Enter c\n"))
#should've added 
x1 = None
x2 = None

#If a is zero, then it is not a quadratic euqation
if a == 0:
    #should've added
    if b != 0 :
        x1 = -c/b
        x2 = -c/b
        print(x1, x2)
    else:
        print("Not valid equation")
else:
    if 4*a*c <= b**2:
        x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
        print("There is no possible solution")
print("The value of x1 is:\n", x1, "\nThe value of x2 is:\n", x2)


'''age=17
#1 just if statement
#2 if-else statement
if age >= 18:
    print("you can drive")

else:
    print("you can't drive")'''


age = int(input("enter age"))

if age <=90 and age >=18:
    print("You are eligeble to drive")
else:
    print("You are not eligible to drive",
          "or have a driver's license",
          "for more info please visit our website")