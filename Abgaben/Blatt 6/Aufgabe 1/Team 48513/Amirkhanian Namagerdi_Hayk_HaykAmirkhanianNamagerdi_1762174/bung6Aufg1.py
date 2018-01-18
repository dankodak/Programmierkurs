import numpy as np
from math import tan
import math
import matplotlib.pyplot as plt
x = np.linspace(0, 10,)
g = 10
y = 10
v = 10
def f(x):
    a = (9.81*x*x)/(math.cos((g*(math.pi))/180) * math.cos((g*(math.pi))/180))
    b = x * tan((g*(math.pi))/180)
    c = (1/(2*v*v))
    d = a * c
    f = b - d + y
    return f
z = f
i = np.linspace(0,10)
plt.plot(i,f(i))
plt.ylabel("Höhe der Kugel")
plt.xlabel("Verstrichene Zeit")
plt.show()

