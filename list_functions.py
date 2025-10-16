#len
nums = [1,8,5,2,3,3,4,5]
n = len(nums)
print(len(nums))

#count function

print(nums.count(4))

#list function
numbers = list(range(11))
T = (1,2,3,4,5)
L = list(T)

for n in numbers:
    print(n,end =" ")

for t in L:
    print(t, end =" ")

#pop, remove and del
#remove removes the value
print(nums)
nums.remove(4)
print(nums)
del nums[4]
print(nums)
nums.pop(0)
print(nums)