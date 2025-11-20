# inline functions are functions that don't need to be copied to memory
# just a line of code

x = 3+1

def add():
    x= 3+1

def add(x,y):
    return x+y
print(add(3,4))

add = lambda x,y : x+y # function handle is value
#This lamda function is equivilent to one above
nums = [1,2,3,4]
add_one = lambda x : x+1
new_nums = map(add_one, nums)
print(nums)
print(new_nums)
add(2,4)