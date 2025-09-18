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
num_as_num = int(num_a_text)

print(num_a_text, type(num_a_text))
print(num_as_num)

num = 3
num_f = float(3)

num2 = 3.4
num2_i = int(num2)

num2_as_text = str(num2)