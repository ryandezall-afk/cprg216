# we are checking for leap year
# A year is a leap year if it is divisible by 4
# but not divisible by 100 unless it is also divisible by 400

year = float(input("Please enter a year:\n"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(int(year), "This is a leap year")
else:
    print("This is not a leap year")

# first we ask for user input of year
# then we check if that number is divisible by 4, 
# not divisble by 100 or divisible by 400.
# if those conditions are met then it is a leap year.
# if it doesn't it is not a leap year.
# In this case () is not necessary 
# But it is good for simplicity and understanding because it may not always work out the way you want without parenthesis.
