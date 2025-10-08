print(list(range(1, 11)))

for n in range(1, 11):
    print("Hello")
    print(n)

print("End of the loop")

for n in range(-5, 11): #if i don't give the starting rang it will start from 0
    result = n * 10
    print("10 x", n, "=", n*10)

print("End of the loop")

for n in range(2, 11, 2): #if i don't give the starting rang it will start from 0
    result = n * 10
    print("10 x", n, "=", n*10)

print("End of the loop")

for i in range(1, 11): #if i don't give the starting rang it will start from 0
    for j in range (1,11):
        print(i, "x", j, "=", i*j, end="")
    print("")