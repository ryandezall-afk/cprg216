# this is our third class demo
'''
In this class we will work on 
variables, and operators, and other stuff
'''
# review
# assignment

x = 3                                       #int
y = 5.3                                     #float
b = True                                    #bool
c = "Hello my name is ryan"                 #str
user_input = input("What is your name?")    #str

print(x, type(x))
print(y, type(y))
print(b, type(b))
print(c, type(c))
print("Hello my name is", user_input, type(user_input))
print("THe value of x * y is:", x*y, "and the type of x is:", type(x), "and the type of y is:", type(y))

# some functions call : print, input, int, float, str, bool,

#&&&&&&&&&&&&&
# casting (changing one type into another, ex. int - float)
# when we do it manually we call it explicit casting
# changing int to float is increasing size (promotion)
# int size is 4 bytes, float is 8 bytes
#&&&&&&&&&&&&&

num_a_text = "43"
num_as_num = int(num_a_text) #converting string to num

print(num_a_text, type(num_a_text)) #will print as a text
print(num_as_num) #will it print???
print(str(num_as_num)) # equivalent to one above, this happens in background of the one before

num = 3
num_f = float(3)

num2 = 3.4
num2_i = int(num2)

num2_as_text = str(num2)


# Using input function.. Note input function always return a string (text)

user_input = input("Please enter your year of birth\n")
year_of_birth = int(user_input)
print("Your age is ",2025 - year_of_birth)


# print function
    #working with a separator

#ESCAPE CHARACTERS
#n (another line
#t (andother tab)
#\'
#\\
#\"

print("Hello", "world", sep=' ', end=' ')
print("Hello", "world", sep=' ')
print("Hello\tworld")
print("Hello\nworld")
print("what is the student's name?")
print('what is the student\'s name?')
print('Use this symbol \\ to make an excape character')



#precedence rules
# multiplication and division come before addition and subtraction
# if 2 that are equal are on same line you go from left to right

expression = 3+4*0-300+12/3
print(expression)

expression = 4/2*3
print(expression)


# More about Assignment

x = 3
x = x + 5
print(x)

#we can have a shorthand for this expression?\

x +=5 # x = x+5
print(x)
#other expressions

x -= 2 # x = x-2
print(x)
x *= 3 # x = x*3
print(x)
x /= 2 # x = x/2
print(x)
x **= 4 # x = x ** 4
print(x)