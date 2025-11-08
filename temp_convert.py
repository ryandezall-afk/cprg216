'''
This function 
'''

def celsius_to_fahernheit(C):
    F = (9/5) * C + 32
    return F


def fahernheit_to_celsius(F):
    C = (F -32) * 5/9
    return C

print(celsius_to_fahernheit(5).__doc__)
print(fahernheit_to_celsius(6))