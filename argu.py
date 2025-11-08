#demo for positional arguments
def get_age(name, yob):
    print("Welcome,", name)
    age = 2025-yob
    print('youre age is', age)

get_age("John", 2000)

#. get_age(2003, "Tom")
#error bc it will take 2003 as name and "Tom" (string) as number or yob

#keyword arguments
get_age(yob=2003, name="Tom")
#if you define them position does not matter. These are keyword instead of positional.

print("Hello", "world", end="")
#print(end="", "hello", "world")

# default / optional arg

def pow(x, y=2):
    print(x**y)

pow(2,3)
pow(3,2)
pow(4)
#so for pow(4) by defning y=2 i believe we have set y to 2 so if only one value is given x becomes that number and y defaults to 2. if pow(4,3) then you are redefining 3.

def write_settings(file="settings.config"):
    fid = open(file, 'w')
    fid.write("screensize: 1808 2876")
    fid.close()

write_settings()
write_settings("mysettings")

def read_setting(file="settings.config"):
    fid=open(file, 'r')
    print(fid.readline())
    fid.close()

read_setting()

# demo for variable length algorithyms

def my_sum(*nums):
    sum = 0
    for num in nums:
        sum += num

    print(sum)
    return sum

my_sum()
my_sum(4)
my_sum(5,67)

# variable length keyword args

def print_info(**kwargs):
    for k, v in kwargs.items():
        print(k,v)


print_info(name="John", age=20, gpa=3.8)
print_info(make="honda", year=2006, model="civic", price=3457)

import util 