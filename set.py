numbers = {1,2,3}
names = set()
print(names)
print(numbers)
names.add('John')
names.add('John')

print(names)

# to review from tuple to list
data = (1,2,3)
dataset = set(data)
print(dataset)

text = "Hello world, what is up" # more like a tuple
unique = set(text)
print(unique)

unique.remove('H')
print(unique)

for ch in unique:
    print(ch, end="\t")
print()

print(min(dataset))
print(max(dataset))
print(len(unique))

'''x = 4
del x
print(x)
del dataset
print(dataset)'''

del dataset
dataset = {3,4,5,8}
print(dataset)

x = 3
print(x)
del x
x = "Hello"
print(x)

num1 = {1 ,2 ,3}
num2 = {1,2,3,4}
'''
num3 = num1.intersection(num2)
num4 = num1.union(num2) 
num5 = num1.difference(num2)
num6 = num2.difference(num1)'''
num3 = num1 & num2
num4 = num1 | num3
num5 = num1 - num2
num6 = num2 - num1
print(num3)
print(num4)
print(num5)
print(num6)

data = {1, 2, 3, 4, 5}

# Bitwise operator
n = 4 & 3
print(n)

# 4: 0 0 0 0 0 1 0 0
# 3: 0 0 0 0 0 0 1 1

set1 = {1,2,3,4,5,6,7}
set2 = {2,3,4}

print("is set2 subset of set1?", set2.issubset(set1))


#Creating set

# Empty set
names = set()
print(names)  # Output: set()

# Set with values
nums = {1, 2, 3}
print(nums)  # Output: {1, 2, 3}


#Adding values to set
names = set()

names.add("John")
names.add("Mary")
names.add("John")  # duplicate

print(names)
# Output: {'John', 'Mary'}
# Notice: John only appears once


# removing values
names = {"John", "Mary", "Alex"}

names.remove("Mary")
print(names)  # {'John', 'Alex'}

names.discard("NotExist")  # safe remove (no error)

#sets authomatically remove duplicates
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  
# Output: {1, 2, 3}


#converting to set
#list - set
data = [1, 2, 2, 3, 4, 4]
unique = set(data)
print(unique)  # {1, 2, 3, 4}

#tuple to set
data = (1, 1, 2, 3)
unique = set(data)
print(unique)  # {1, 2, 3}


#set from a string
text = "Hello World"
letters = set(text)
print(letters)
#(output) {'H', 'e', 'l', 'o', ' ', 'W', 'r', 'd'}


#sets are unordered
print(set("hello"))
print(set("hello"))



#basic set operations

#union (combine values)
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) 
# {1, 2, 3, 4, 5}

#intersection
print(a.intersection(b))  
# {3}

#difference
print(a.difference(b))
# {1, 2}



#membership test
a = {10, 20, 30}
print(20 in a)  # True
print(5 in a)   # False


#Basic Membership test
students = {"John", "Sara", "Alex"}

name = "Sara"

if name in students:
    print(name, "is in the class!")
else:
    print(name, "is NOT in the class.")


#INput example
students = {"John", "Sara", "Alex"}

name = input("Enter a name: ")

if name in students:
    print("Student exists in the list.")
else:
    print("Student not found.")


#not in set
banned_words = {"spam", "scam", "fake"}

word = "hello"

if word not in banned_words:
    print("Word is allowed")
else:
    print("Word is blocked")


#example with numbers
lucky_numbers = {3, 7, 9}

num = 5

if num in lucky_numbers:
    print("Lucky number!")
else:
    print("Not lucky.")


#best practice trick
colors = {"red", "blue", "green"}
choice = "blue"

exists = choice in colors

print(exists)  # True




