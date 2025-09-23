print("Hello, welcome to the party software..")
name = input("Please Enter your name:\n")
if name == 'cat':
    name = 'Cat'

print("Welcome,", name)
print("TO have a drink you need to provide your age")

age = int(input("What is your age?"))

is_adult = age >= 18

if is_adult:
    print("you are allowed to have a drink..")
else:
    print("sorry, you are a child")