import numpy as np
import math as m
import matplotlib.pyplot as plt
n=int(input("n="))
q=1
A=[]
while q<=n:
    w = 1
    while w<=n:
        a=int(input("a{}{}=".format(q,w)))
        A.append(a)
        w +=1
    q += 1
A=np.array(A)
A.shape=(n,n)
q=1
B=[]
while q<=n:
    w = 1
    while w<=n:
        b=int(input("b{}{}=".format(q,w)))
        B.append(b)
        w +=1
    q += 1
B=np.array(B)
B.shape=(n,n)

p=0
k=0
C=[]
while p<n:
    k = 0
    while k<n:
        f=0
        t=0
        while f<n:
            CC=A[p][f]*B[f][k]
            t+=CC
            f+=1

        C.append(t)
        k+=1
    p+=1
C=np.array(C)
C.shape=(n,n)
print(C)
