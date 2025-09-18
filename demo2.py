x = 5 # assignment statement
print(x) # function call
#function is a block of code written somewhere else that you are just calling to do something for you

# variables
# variable has a name
# , has a value
# , has an address
# , has a size
# , and has a type
# if you know the size you know the type, vice versa


#these are all types
i = 3 # int (integers or whole numbers)
f = 4.5 #float (real numbers that have a deciaml point, 4.5 is a float but 4 is not and vice versa for int)
b = True # Boole (true or false)
s = "hello" #string (strings are created by enclosing characters in "..." or '...')
msg = 'Hello world!'
ch = 'a' # it is still a string 

print(i, type(i))
print(f, type(f))
print(s, type(s))
print(msg)
print(b)
print(ch)

#variable names
#can be using letters, digits and _ (you can't have a comma in a name for example)
#it can't start with a number
#it can start with _ but you shouldn't use it (because it has a different meaning)
# use  meaningful variable name

#example
circle_radius = 5
PI = 3.14
circle_radius = 6
area_of_circle = PI * circle_radius * circle_radius

print("The area of the circle is:", area_of_circle)

#Operations

a = 3+4
b = 4-3
c = 4*3
d = 3/4
d_ = 3//4 # floor division
e = 4%3 # the result is the remainder after division
f = 3**3 # power (this would be 3^3)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))

# combining variables

e = a+b # process the assignment from right to left
# it means evalue a+b first, then add the result

print("the value of e is:", e)

#static type vs dynamic type

x = 5 #type int
x = 4.3 # x changed its type to be float
x = "hello" # x changed to str
x = True # x changed to Boole

# casting

x = 3 #int
y = 4 #int
z = x/y #float, automatic casting

print(z)

# manual casting (explicit casting)

int(z)
print(int(z))

print(int("43"))

print(str(43))

x = 1
print(x, type(x))

y = float(x)
print(y, type(y))

v = 4.3
print(v, type(v))
u = int(v)
print(u, type(u))  # demotion

#putting type inside the print command just mean it will print the value of that letter as well as what type it is