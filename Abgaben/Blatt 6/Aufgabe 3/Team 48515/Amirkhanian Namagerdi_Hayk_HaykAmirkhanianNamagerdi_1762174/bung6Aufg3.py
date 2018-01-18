import numpy as np
import matplotlib.pyplot as plt
n = 100
l = 0,5
fo = 200
ul = 42
ur = 10
f = [ul]
for x in range (n-2):
    dx = x/(n-1)
    deltax = dx * dx
    f.append(deltax * fo)
f.append(ur)
g = np.array(f)
p = [1]
for x in range (n-2):
    p.append(2)
p.append(1)
a = np.array(p)
w = [0]
for x in range (n-2):
    w.append(-1)
r = np.array(w)
t = []
for x in range (n-2):
    t.append(-1)
t.append(0)
A = np.zeros((100,100)) + np.diag(a,0) + np.diag(r,1) + np.diag(t,-1)
C = np.array(A)
u = np.linalg.solve(C,f)
print(u)
z = []
for i in range (n):
    z.append(i*deltax)
plt.plot(u,z)
plt.show()






