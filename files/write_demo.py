'''def write(file, msg):
    fid = open(file, 'a')
    fid.write(msg)
    fid.close()

write("testFile",'hey there')
write("testFile", 'hey')'''

fid = open("myfile.tx", 'w')
students = ["sam \n","john\n","gary\n"]
fid.writelines(students)
fid.close()