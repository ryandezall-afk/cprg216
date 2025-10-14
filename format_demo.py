yesterday_value = 0.7588
today_value = 0.7479
change = today_value - yesterday_value

print(f"{'Date':>10s}{'Rate':>10s}")
print(f"{'====':>10s}{'====':>10s}")
print(f"{'Yesterday':>10s}{yesterday_value:>10.4f}")
print(f"{'Today':>10s}{today_value:>10.4f}")
print(f"{'Change':>10s}{change:>10.4f}")

names = ["John", "Doe", "Jane", "Smith"]
GPA = [3.5, 3.7, 3.9, 4.0]

print(f"{'Name':<5s}{'GPA':>7s}")
print(f"{'====':<5s}{'===':>7s}")
for i in range(4):
    print(f"{names[i]:>5s}{GPA[i]:>7.2f}")

for name, gpa in zip(names, GPA):             #I believe his didn't work because he has to zip the the lists
    print(f"{name:>5s}{gpa:>7.2f}")