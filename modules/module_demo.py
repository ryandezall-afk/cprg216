# import math
import statistics as st
from math import cos, sqrt
import os
from util import *
import util

def fact(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result
    
def cos(x):
    result = 0
    x = x * (22/7)/180
    for n in range(0,50):
        result += ((-1)**n) * (x**(2*n))/(fact(2*n))

    return result

print(fact(5))
print(cos(30))
print(cos(30 * (22/7)/180))
print(sqrt(9))

data = [31, 28, 29, 34, 25]
print(st.mean(data))
print(st.stdev(data))

write("myFile", "Hello")