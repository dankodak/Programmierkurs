import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from math import sqrt,pi,exp

sigma_values = [0.2, 1.0, 5.0]
mu = 0
linestyles = ['-','--',':']

x = np.linspace(-5, 5, 1500)

for sigma, ls in zip(sigma_values,linestyles):
    N  = norm(mu, sigma)

    plt.plot(x,N.pdf(x),ls=ls, c='black',
             label = (mu, sigma))
plt.xlim(-5, 5)
plt.ylim(0, 2.2)

plt.xlabel("x")
plt.ylabel("N(x, sigma,mu)")
plt.title("Gauß-Verteilung")

plt.legend()
plt.show()
 