import numpy as np
import matplotlib.pyplot as plt
def cannon (y,o,v):
    x=np.array([0,1,2,3,4,5,6,7,8,9,10])
    return (x*np.tan(o*np.pi/180)-((9.81*(x**2))/(2*(v**2)*(np.cos(o*np.pi/180))**2))+y)

print ("bitte y0 eingeben")
y = int(input())

print ("bitte θ eingeben")
o = int(input())

print ("bitte V0 eingeben")
v = int(input())

plt.plot(cannon(y,o,v))
plt.show()
