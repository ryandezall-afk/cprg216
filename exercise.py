grade = int(input("Enter grade"))
if grade >= 90:
    print("you got an A")
elif grade >= 80:
    print("you got b")

grade = int(input("Enter grade"))
letter_grade = "A"
match grade:
    case 90:
        letter_grade = "A"
    case 80:
        letter_grade = "B"
    case 70:
        letter_grade = "C"
    case 60:
        letter_grade = "D"
    case 50:
        letter_grade = "F"
print(letter_grade)

#Exercise Leap Year
