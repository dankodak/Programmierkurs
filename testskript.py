import numpy as np
import matplotlib.pyplot as plt
n = int(input("Wie groß soll die nxn-Matrix sein?   n="))
C=[]
u_l=42
u_r=10
f0 = 200
l = 0.5
dx=l/(n-1)
for t in range(n):
    C.append(np.linspace(0, 0, n))
for o in range(n):
    if o==0:
        C[o][o]=1
    elif o==n-1:
        C[o][o]=1
    elif o>0 and o<n-1:
        C[o][o-1]=-1
        C[o][o]=2
        C[o][o+1]=-1
f=[]
for h in range (n):
    if h==0:
        f.append(u_l)
    elif h==n-1:
        f.append(u_r)
    else:
        f.append((dx**2)*f0)
u=np.linalg.solve(C,f)
xi = i*dx
for i in range (n):
    plt.plot(u[i],xi)
    plt.xlabel("x")
    plt.ylabel("u")
    plt.legend()
    plt.show()
print(C)
print(f)
print(u)