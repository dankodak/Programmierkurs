import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from math import sqrt,pi,exp

sigma_values = [0.2, 1.0, 5.0]
mu = 0
linestyles = ['-', '--', ':']

x = np.linspace(-5, 5, 1337)

for sigma, ls in zip(sigma_values,linestyles):
    N = norm(mu,sigma)

    plt.plot(x, N.pdf(x), ls=ls, c='black',
             label = (mu, sigma))

plt.xlim(-5, 5)
plt.ylim(0, 2.2)

plt.xlabel("x")
plt.ylabel("N(x,sigma,mu)")
plt.title('Gauß-Verteilung')

plt.legend()
plt.show()

#ich hab's jetzt so gemacht, da mit der Formel:
#N = 1 / sqrt(2 * pi * sigma ** 2) * exp((-(x - mu) ** 2 / 2 * sigma ** 2))
#andauernd dieser Fehler kommt: "only length-1 arrays can be converted to Python scalars"