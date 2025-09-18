# I want to compute the circum and area of the circle
# assume the circl radius is 5
# modify : ask user to enter the circle radius
# assume that pi = 3.14

#mine
circle_radius = 5 
pi = 3.14
circum_given = 2
input("Please enter the radius of the circle:")

area_of_circle = pi * circle_radius * circle_radius
circum_of_circle = circum_given * pi * circle_radius
print("the area of the circle is:", area_of_circle)
print("the circumference of a circle is:", circum_of_circle)

# his code
r = 5
PI = 3.14
#PI = 1313.22 # logical error, cause if you want pi to be constant, it has to be (not sure what he said from here) 3.14 or the same value
#r = input("Please enter the radius of circle:")
user_input = input("Please enter the radius of circle:")
print("Type of user input", type(user_input))
r = int(user_input)
circle = 2 * PI * r
area = PI * r ** 2
print(circle)
print(area)


#my code wasn't meant to be as extreme as his
#mine was right just a little more complex than it really had to be


