
print("Welcome to the quadratic equation solver!")
option = "Yes"
while option == "Yes":
    print("Please enter three numbers a, b and c")
    a = float(input("enter A:\n"))
    b = float(input("enter B:\n"))
    c = float(input("enter C:\n"))

    x1 = None
    x2 = None

    if a == 0:
        if b == 0:
            print("No solution")
        else:
            x1 = x2 = -c / b
            print(x1)
    else:
        det = b**2 - 4*a*c
        if det >= 0:
            x1 = (-b + det**0.5) / (2*a)
            x2 = (-b - det**0.5) / (2*a)
            print("Solution for x1 is:", x1, "and for x2 in:", x2)
        else:
            print("No real solution")
    option = input("Do you want to continue? Yes/No\n")

