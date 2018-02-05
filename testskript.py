import numpy as np
import matplotlib.pyplot as plt

def parameterLGS(w):
    return np.array([[1,-1],[w/3,-1]]),np.array([[-1],[-2+2*w]])

def solveLGS(A,b):
    inverse = 1/(A[1,1]*(A[0,0]-A[1,0])) * np.array([[A[1,1], -A[0,1]], [-A[1,0], A[0,0]]])
    return inverse@b

A,b = parameterLGS(2)
print(solveLGS(A,b))