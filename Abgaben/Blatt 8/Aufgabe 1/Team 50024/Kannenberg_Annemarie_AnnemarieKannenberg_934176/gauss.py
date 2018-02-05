import math as m
import numpy as np
import matplotlib.pyplot as plt

n = 100
mu = np.array([0,0,0,-2])
sigma = np.array([0.2,1,5,0.5])
x = np.linspace(-5,5,n)

allN = np.zeros((n, 4))

for i in range(0,4):
    N = 1/(2*m.pi * sigma[i]**2)**(1/2)* np.exp(- (x-mu[i])**2/(2*sigma[i]**2))
    plt.plot(x,N, label="sigma=%f, mu =%f"%(sigma[i],mu[i],))
plt.ylabel('y')
plt.xlabel('x')
plt.title('Gauss-Verteilung')
plt.legend(loc='best', ncol=1, shadow=True, fancybox=True)
plt.show()



