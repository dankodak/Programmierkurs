#Aufgabe 1
import math
import numpy as np
import matplotlib.pyplot as plt
I = float(input("Geben Sie die initiale Geschwindigkeit ein:"))
A = float(input("Geben Sie die y-Koordinate des Abschusswinkels ein:"))
O = float(input("Geben Sie den Abschusswinkel ein:"))
if 0<= O <=90:
    x = np.linspace(0,10)
    y = ((x*math.tan(O*math.pi)/180)) - ((9.81*(x**2))/(2*(I**2)*(math.cos((O*math.pi)/180))**2)+A)
    plt.plot(x, y, "m")
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.title("Flugbahn einer Kanonenkugel")
    plt.show()
else :
    print("Sie haben eine falsche Zahl eingegeben")
