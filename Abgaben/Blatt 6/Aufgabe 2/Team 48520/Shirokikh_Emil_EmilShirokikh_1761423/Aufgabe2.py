#Aufgabe2    Emil Shirokikhssss
# a)

import time
import numpy as np
import random
from math import sin , cos


def matrix_multiplication(A, A2):
    al = len(A)
    a2w = len(A2[0])
    result = np.zeros((al, a2w))
    for i in range(len(A)):
        for j in range(len(A2[0])):
            for k in range(len(A2)):
                result[i][j] += A[i][k] * A2[k][j]

    return result

# ist nach dem selben Schema erweiterbar - die Matrizen
#muessen dafuer auch nicht gleich gross sein sondern die erste
#Matrix muss gleich viele Spalten wie die 2e Matrix Zeilen
#haben.

#b)
def time_it(func, m = 10):
    # Diese function ist die gleiche, wie die aus der Vorlesung 6 Seite 29
    tstart = time.clock()
    for i in range(m):
        func
    return (time.clock() - tstart)/m

A = np.ones((100,100))

print(time_it(matrix_multiplication(A,A)))
print(time_it(np.dot(A, A)))


