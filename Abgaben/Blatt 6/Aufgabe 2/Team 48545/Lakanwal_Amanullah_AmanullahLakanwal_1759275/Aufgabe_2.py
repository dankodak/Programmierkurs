import time
import numpy as np
from math import sin, cos
def time_it(func, m=100):

    tstart = time.clock()
    for i in range(m):
        func()
    return (time.clock() - tstart)/m

def C_matrix_multiplication():
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))]]
            for col_b in zip_b] for row_a in a]


def matrix_multiplication():
        C = np.dot(a,b)
        return (C)
tstandard = time_it(C_matrix_multiplication)
tnumpy = time_it(matrix_multiplication)

print("Dauer für Matrizenmultiplikation in Python:",tstandard)
print("Dauer für Matrizenmultiplikation in NumPy:",tnumpy)
print("numpy ist",tstandard/tnumpy,"mal schneller!")


