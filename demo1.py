#naming a variable
# start with a letter
# you can include digits and underscore and letters
# can't start with a digit
# a convention a traditional way of doing something
# there is a convention for python names of variables

book_id = 1234
cat_color = 'red'
greeting_message = "Hello"

ghdfhsgdshg = 4 #unconventional can be named this way but doesn't make any sense

print(ghdfhsgdshg) #not following the convention


#logical error
v = 3 # v is assigned 3

u = v == 2 # v is assigned 2
#this is an equality check v==2, it is a question asking if v=2
#the answer to this question is the value of the expression
z = 2 + u

print(z)

#runtime error
user_input = input("What is your age?")
after = int(user_input) + 5
print("After five years your age will be ", after)