import numpy as np
import matplotlib.pyplot as plt
from math import tan, cos, pi, radians

n = 9999

# wenn ich den Input einschränke, lande ich in einer endlosen Schleife
while True:
    try:
        y0 = float(input("Bitte geben Sie eine Zahl für die Höhe der Kanone ein: "))
#        if y0 in range(0,n):
#            continue
#        else:
#            print("Number below 0!")

        T = float(input("Bitte geben Sie eine Zahl zwischen 0 und 90 für den Abschusswinkel zwischen der x-Achse und dem Kanonenrohr ein:  "))
#        if T in range(0,90):
#            continue
#        else:
#            print("Number out of range!")

        v0 = float(input("Bitte geben Sie eine Zahl größer als 0 für die Anfangsgeschwindigkeit an: "))
 #       if v0 in range(0,n):
 #           break
 #       else:
 #           print("Number below 0!")
        break

    except:
            print("Das ist keine Zahl!")

# x-Achse geht von 0 bis 10, in 1000er Schritten
x = np.linspace(0, 10, 1000)
g = 9.81

# Formel für Kurvenbahn der Kanonenkugel
y = x * tan(radians(T * pi / 180)) - (1 / (2 * (v0**2))) * (g * (x**2) / (cos(radians(T * pi / 180))**2)) + y0

plt.plot(x, y)
plt.xlabel("Weite(x)")
plt.ylabel("Höhe(y)")
plt.title("Kurvenbahn einer Kanonenkugel")
plt.show()