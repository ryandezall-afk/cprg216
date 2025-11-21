import os

print("current working directory", os.getcwd)
cwd = os.getcwd

file = os.path.join(cwd,"demo.txt")
exists = os.path.exists(file)
print(exists)
