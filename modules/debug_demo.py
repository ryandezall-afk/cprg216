from util import write
def modify_list(data):
    for i in range(0,len(data)):
        data[i] *=2


print("hello welcome to the debugger testingg...")

x = 3+1
y = x **3
y = y*2
condition = y == 128
nums = [1,2,3,4]

modify_list(nums)
print(nums)

write("myFile",'this is a test')

print(condition)