from math import sqrt, ceil

def eras(nmax):
    return {i for i in range(2,nmax+1)} - {k*i for k in range(2,ceil(sqrt(nmax))+1) for i in range(2,ceil(nmax/k)+1)}
print(eras(20))