# the print function can take several argument.

print("Helloo", 1, 2.6, True)
msg = "Hello" + " World"
print("Helloo" + " World")  


name1 = "John"
name2 = "Doe"
print (name1, name2, sep=",")
print("Done")

#formatting
#format()
#format()

print(format(33877845.23432343, ',.2f'))
print(format(33877845.23432343, '.2e'))
print(format(0.33, '%'))
print(format(124, 'd'))
print(format("Hello", 's'))

mesg = format(33877845.23432343, ',.2f')
print(mesg)

#second for of format
#"hello".format()
x=3
y=4.3
z=3.55
print("The value of x is", x ,"and y is", y)
print("The value of x is {} and y is {:.2f}".format(x,y))
print("The value of y is {1:.3f} and x is {0:.2e} and z is {2:.1f}".format(x,y,z))
print("the value of x is {:d}" .format(x))
name="John"
text = "Hello, {}. Welcome!" .format(name)
print(text)
print("Hello, {:s}. Welcome!" .format(name))

#third way to format a string
print(f"x is {x:d}, y is {y:.4f}")
print(f"x is {x}, y is {y}")
print(f"x is binary {x:b}")
print(f"x is binary {x:x}")
name1="John"
name2="Doejrjunior"
age1 = 20
age2 = 21

print(f"{name1:s} {age1:d}")
print(f"{name2:s} {age2:d}")
#align right
print(f"{name1:>11s} {age1:<3d}")
print(f"{name2:>11s} {age2:<3d}")

print(f"{name1:>11s} {age1:<3d}")
print(f"{name2:>11s} {age2:<3d}")
title = "Age table"
print(f"{title:^19s}")