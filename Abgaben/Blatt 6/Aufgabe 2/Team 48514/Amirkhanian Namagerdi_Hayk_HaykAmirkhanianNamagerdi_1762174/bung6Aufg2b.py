import time
import numpy as np
import random
A = np.ones( (100,100) )
B = np.ones( (100,100) )
def time_it(func, m=10):
    tstart = time.clock()
    for i in range(m):
        func()
    return (time.clock() - tstart) / m
def mm():
    C = []
    for g in range (len(A)):
        for f in range (len(A)):
            e = 0
            for b in range (len(A)):
                e = e + A[g][b] * B[b][f]
            C.append(e)
    return C
def num():
    G = np.array(A).dot(np.array(B))
    return G
print(mm())
print(num())
print(time_it(num))
print(time_it(mm))

