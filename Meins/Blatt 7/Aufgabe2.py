import numpy as np

A = np.reshape(np.array(range(1,101)),(10,10))

print(A[9,:])
print(A[1:9,1:9])
print(A[:,1::2])
print(np.diagonal(A))