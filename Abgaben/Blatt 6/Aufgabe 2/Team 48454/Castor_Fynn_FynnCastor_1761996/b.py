import numpy as np
import time
def annoyance(A):
    p=0
    k=0
    C=[]
    while p<100:
        k = 0
        while k<100:
            f=0
            t=0
            while f<100:
                CC=A[p][f]*A[f][k]
                t+=CC
                f+=1

            C.append(t)
            k+=1
        p+=1
    C=np.array(C)
    C.shape=(100,100)
    print(C)
l=10
A=np.ones((100,100))

tstart=time.clock()
for ö in range(l):
    annoyance(A)
s= (time.clock()-tstart)/l
print(s)


tstart=time.clock()
for ö in range(l):
    np.dot(A,A)
s= (time.clock()-tstart)/l
print(s)