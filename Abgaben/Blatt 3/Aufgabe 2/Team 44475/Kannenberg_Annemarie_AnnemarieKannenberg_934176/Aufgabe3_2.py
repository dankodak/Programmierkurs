import numpy as np


def pascal(n):
    P = []
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    # if n==3:
        # P = [1,pascal(2)[0]+pascal(2)[1],1]
        # return P
    # if n==4:
        # P = [1,pascal(3)[0]+pascal(3)[1],pascal(3)[n-3]+pascal(3)[n-2],1]
        # return P
    P[0:0] = [1]
    for i in range(1,n-1):
        #print(i)
        P[i:i] = [pascal(n-1)[i-1]+pascal(n-1)[i]]
    P[n-1:n-1] = [1]
    return P
        
x = pascal(5)

print(x)