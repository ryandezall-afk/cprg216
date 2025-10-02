number = 1
sum = 0
while number <= 100:
    sum += number
    print(sum)
    number += 1

# 1. start with number = 1 or 0
#    sum = 0
# 2. increase number by 1 until it reaches 100
# 3. add number to sum
# 4. repeat step 2, 3, 4 until number is 100

number = 0
sum = 0
while number < 100:
    number += 1
    sum += number
print(sum)

# n(n+1)/2
# n = 100
n = 100
sum = n * (n + 1) / 2
print(sum)

# sum = number * (number + 1) / 2

number = 0
fact = 1
while number < 5:
    number += 1
    fact *= number
print(fact)

