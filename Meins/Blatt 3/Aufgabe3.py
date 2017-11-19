import time
from math import fabs
def standard(a,x):
    result = 0
    pot = 1
    for val in a:
        result += val*pot
        pot *= x
    return result

def horner(a,x):
    b = 0
    a = a[::-1]
    for val in a:
        b = val + b*x
    return b

a = range(-50,51)
x = 4.12
start=time.clock()
for i in range(1000):
    standard(a,x)
end = time.clock()
print(fabs(start - end))

start=time.clock()
for i in range(1000):
    horner(a,x)
end = time.clock()
print(fabs(start - end))