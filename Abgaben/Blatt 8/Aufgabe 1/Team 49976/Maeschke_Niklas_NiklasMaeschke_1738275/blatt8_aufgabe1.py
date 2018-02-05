import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.0,5.0,0.01)
for a in [[0,0.2],[0,1],[0,5],[-2,5]]:
    u=a[0]
    o=a[1]
    stringu=str(u)
    stringo=str(o)
    gauss=(1/np.sqrt(2*np.pi*o**2))*np.exp(-((x-u)**2)/(2*o**2))
    plt.plot(x,gauss,lw=2,label= "mit μ = "+stringu+  " und σ = "+stringo )
    plt.xlabel("x")
    plt.ylabel("Gaussverteilung")
    plt.title("Gaussverteilung")
    plt.legend()
plt.show()


