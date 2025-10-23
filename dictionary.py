student_data ={"sam":3.4, "john":3.2} # the pair of key values can be of any type
info ={1:'sam', 2:'sam', 3:'john'}

print(student_data)
print(info)

students_gpa= dict()
print(students_gpa)

nums = [1,2,3,4]
nums2 = [1,2,3,4]

print(nums[1])
print(nums2[-1])
print(student_data["sam"])

print(student_data.keys())
print(student_data.values())

avg_temp = {1:28.3,2:23.4,3:25.2}
print(avg_temp)
print(avg_temp.keys())
print(avg_temp.values())
print(avg_temp[3])

for day in avg_temp:
    print(day, avg_temp[day])

for day, temp in avg_temp.items():
    print(day, temp)

avg_temp[8] = 3.4
