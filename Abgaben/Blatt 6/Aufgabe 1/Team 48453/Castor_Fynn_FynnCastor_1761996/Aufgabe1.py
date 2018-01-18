import numpy as np
import math as m
import matplotlib.pyplot as plt
g=9.81
sa=float(input("pls type in a shooting angle betwenn 0° and 90°"))
v0=float(input("pls type in the initial velocity"))
y0=float(input("pls type in the the shooting height"))

x=np.linspace(0,10)
def y(x):
    y=x*m.tan(sa*m.pi/180)-g*x**2/(2*v0**2*m.cos(sa*m.pi/180))+y0
    return y

plt.plot(x,y(x))
plt.ylabel('y')
plt.xlabel('x')
plt.title("H9")
plt.show()