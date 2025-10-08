print("Welcome to the average calculator!")
continue_option = "Yes"
while continue_option == "Yes":
    sum = 0
    print("Please enter any set of numbers.")
    num = 0
    count = 0
    while num != -50:
        count += 1
        sum += num
        num = float(input(""))

    count -= 1  # Adjust count to exclude the sentinel value    
    average = sum / count
    print("The average is:", average)   
    continue_option = input("Do you want to continue? Yes/No\n")

print("Thank you for using the average calculator!")