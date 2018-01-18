#Emil Shirokikh
#Aufgabe1

import matplotlib.pyplot as plt
import numpy as np
from math import cos
from math import tan
from math import pi

x = np.linspace(0,10,500)


def f(x_1, v_0, y_0, t):
    g = 9.81
    y = (x_1 * tan((t* pi) / 180)) - ((g * x_1 ** 2) / ((2 * (v_0 ** 2)) * (cos(t * pi / 180) ** 2))) + y_0
    return y





print("Geben Sie bitte y_0 ein!")
y_0 = float(input("y_0:"))
print("Geben Sie bitte Theta(Einen Winkel von 0Grad bis 90Grad ein!")
theta = float(input("Theta:"))
print("Geben Sie bitte v_0 ein!")
v_0 = float(input("v_0:"))
A=f(x,v_0,y_0,theta)

temp = np.where(A[:] > 0.)[0][0:]
s = len(temp)

splitted = np.split(x,[s])

x1 = splitted[0]
x2 = splitted[1]

plt.plot(x1, f(x1, v_0,y_0,theta))
plt.plot(x2, f(x2, v_0,y_0,theta),"r-")
plt.ylabel("Hight of canonball")
plt.xlabel("time")
