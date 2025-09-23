# premitive data types

x = 2 #int
y = 3.4 # float
z = "hello" #string

condition = True # Boolean

# value of an expression

#name = input("Enter your name") # does this have a value: Yes (the user provided value)
age = 2025 - 2005
#print(name, age)

# Boolean expression
# We are trying to answer a question.
# the anser is either yes or no (True or False)
# our anser to this question is the value of the expression

#3 > 4 # is this a boolean expression: Yes 
# We are asking is 3 bigger than 4???? THe answer is No (false)
# Then the value of this expression is false

var = 3 > 4 # Logical expression
# what is the type of var? Boolean
#ANything that is true or false is boolean
print(var)

# choosing the variable name
# by convention people use a question for the variable name of 
# a boolean expression

is_adult = age >= 18
print(is_adult)

# provide three variabe names for boolean variables
is_even = (age %2 == 0) # equality check operator
print ("Age is even?", is_even)
# Logical operators > < >= <= ==

is_absent = True
is_child = False

won = False

# List the logical operators
# larger then >
# larger then or equal >=
# smaller then <
# smaller than or equal <=
# equal ==
# not equal !=

print("is 3>4?", 3>4)
print("is 3<=4?", 3<=4)
print("is 3 equalt to 5?", 3==5)
print("is 5 >= 5?", 5>=5)
print("is age larger than 35?", age>35)
print("are 4 and 5 not equal?", 4 != 5)

# Now let's work on if statement
# if (keyword, is a must)
# boolean expression (is a must)
# : is a must
# indentation (must have)
# one or more statements of any type

if 3>4: # is like then what?
    print("yes")
    print("yes that is true")

print("outside if statement")

# what is a statement? a complete instruction
if 4>5: #not a complete statement
    print(True) # now a complete statement 

month = input("What is your birth month?")
if month == "January":
    print("First month eh")
if month == "Febuary":
    print("Ig you're second for everything huh")
if month == "April":
    print("April fools")
if month == "November":
    print("Are you depressed? Terrible month buddy")
elif month != "January, Febuary, April, November":
    print("loser")

print("welcome to the quadratic equation solver")
print("enter three numbers a, b, c")
a = int(input("enter a:"))
b = int(input("enter b"))
c = int(input("enter c"))

if a == 0:
    x1 = -c/b
    x2 = -c/b
    x1 = x2
    print(x1, x2)
elif 4*a*c < b**2:
    x1 = (-b + (b**2 - 4*a*c) ** 0.5 )/(2*a)
    x2 = (-b - (b**2 - 4*a*c) ** 0.5 )/(2*a)
    print(x1, x2)
else:
    print ("Not possible solution")

#his
print("welcome to the quadratic equation solver")
print("enter three numbers a, b, c")
a = float(input('\n'))
b = float(input('\n'))
c = float(input('\n'))
x1 = 0
x2 = 0
if a == 0:
    x1 = -c/b
    x2 = -c/b
else:
    if b**2 >= 4*a*c:
        x1 = (-b + (b**2 - 4*a*c) ** 0.5)/(2*a)
        x2 = (-b - (b**2 - 4*a*c) ** 0.5)/(2*a)
    else:
        x1 = None
        x2 = None
print("the solution to problem is", x1, x2)
