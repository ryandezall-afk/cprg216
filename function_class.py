def my_max():
    print("please enter two numbers:")
    x = float(input())
    y = float(input())

    if x<y:
        print(y)
    else:
        print(x)

    print("random message")



'''my_max()
my_max()
my_max()
my_max()'''


'''if x<y:
    print(y)
else:
    print(x)
if x<y:
    print(y)
else:
    print(x)
if x<y:
    print(y)
else:
    print(x)

print("random message")
print("random message")

if x<y:
    print(y)
else:
    print(x)

print("random message")'''

def compute_area(r):
    PI = 3.14
    area = PI*r*2
    print(area)

compute_area(1)
compute_area(16) #so changing the value (r) in calling the function will change that in function itself. seems obvious but just to remember.


print(print(3))

x = print(3)
print(x)
#print does not have an output. it's output is none. it will print 3 and then print none.

def my_max(x,y):
    max = y
    if x>y:
        max = x
    return max

print(my_max(3,4))
m = my_max(4,5)
print(m)

l = 4
n = 33
m = my_max(l,n)
print(m)

# 1. a function that takes three arguments and return the maximum of them
# 2. a function that takes a name and year of birth, and print a welcome message and the computed age (it does not return anything)
# 3. a fucntion that computes the square root of an argument

def maximum():
    x = float(input())
    y = float(input())
    z = float(input())

    if x>y and x>z:
        most= x
    elif y>z:
        most = y
    else:
        most = z
    return most

max = maximum()
print(max)

#should have done like...

def maximum(x,y,z):
    if x>y and x>z:
        most= x
    elif y>z:
        most = y
    else:
        most = z
    return most

##########

def welcome():
    print("please enter name and year of birth")
    x = input("Name")
    y = input("year")

    print(x,y)

welcome()

#

def welcome(name,birth):
    age = 2025 - birth
    print(name,age)

##########

def square():
    x = float(input())
    square_root = x*.5
    return square_root

#

def squ(number):
    return number*0.5


sq = square()
print(sq)


def welcome_msg():
    print("WElcome to the student enrolment program")
    print("Please choose from the following options")
    print("1 - Add a new student")
    print("2 - Remove student")

welcome_msg()

