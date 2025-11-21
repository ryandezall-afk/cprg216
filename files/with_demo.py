with open('testFile') as fid:
    for line in fid:
        print(line,end ="")

with open('myFile', 'w') as file:
    file.write("Hey there")