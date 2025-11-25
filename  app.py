from car import *

x = 2
y = 3.4
print(type(x), type(y))

c1 = Car('bmw', 2024, 30000, 'violet', 'suv') # we have to set everything here when we contruct the object
'''
c1.set_color('red')
c1.color = 'red'
print(type(c1))
'''
c2 = Car('kia', 2025, 10000, 'posh', 'suv')
c3 = Car('Hyundia', 2020, 70430, 'silver', 'car')
c4 = Car('chevy', 2004, 300000, 'red', 'truck')
'''
c1.set_everything('honda', 2000, 205000, "matt black")
c2.set_everything('kia', 2015, 20500, "purple")
c3.set_everything('hyundia', 2007, 305000, "polished white")
'''
print(c1.color, c1.make, c1.year, c1.milage, c1.body)
print(c2.color, c2.make, c2.year, c2.milage, c2.body)
print(c3.color, c3.make, c3.year, c3.milage, c3.body)
print(c4.color, c4.make, c4.year, c4.milage, c4.body)

print(c1.__speed)
c1.accelerate()
print(c1.__speed)
c1.accelerate()
print(c1.__speed)
c1.accelerate()
print(c1.__speed)
c1.accelerate()
print(c1.__speed)
c1.decelerate()
c1.decelerate()
print(c1.__speed)
c1.brake()
print(c1.__speed)

c1.decelerate()
c1.decelerate()
c1.decelerate()
c1.decelerate()
print(c1.__speed) #still zero