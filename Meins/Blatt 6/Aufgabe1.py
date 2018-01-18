import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 10
theta = 45
y0 = 0

x = np.linspace(0,10)
fx = x*np.tan((np.pi * theta)/180) - (g*x**2)/(2*(v0**2)*np.cos((theta*np.pi)/180)**2) + y0
plt.plot(x,fx)
plt.show()