import time
import numpy as np

def time_it(func, m = 10):
    tstart = time.clock()
    for i in range(m):
        func()
    return (time.clock() - tstart) / m

def numpy(A = np.ones((100,100))):
   C = np.dot(A, A)
   return C

def matrix_multiplication(A = np.ones((100,100))):
    [I, J] = A.shape
    C = np.zeros((I, J))
    for i in range(I):
        for j in range(J):
            C[i, j] = C[i, j] + A[i, j] * A[j, i]
            return C

tnumpy = time_it(numpy)
tmatrix_multiplication = time_it(matrix_multiplication)

print("Time numpy:",tnumpy)
print("Time matrix_multiplication:",tmatrix_multiplication)
print("matrix_multiplication is",tnumpy/tmatrix_multiplication,"times faster than numpy!")








