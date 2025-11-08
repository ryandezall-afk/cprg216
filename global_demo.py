g_var = 3

def mysum():
    i_var =3
    print(g_var)
    print(i_var)

print(g_var)
# print(i_var)
#can't print because it in thingy

def mysum():
    i_var =3
    global inside_global
    inside_global = 4
    print(g_var)
    print(i_var)

mysum()
print(g_var)
print(inside_global)

import util
util.write_to_file("demo.txt","just a demo")

util.read_to_file("demo.txt")
