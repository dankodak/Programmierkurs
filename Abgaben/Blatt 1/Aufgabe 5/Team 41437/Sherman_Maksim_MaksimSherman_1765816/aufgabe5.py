import math

x = 0.-5000
sinx = math.sin(x)
Fehler = math.fabs(x-sinx)

n = float(input("Anzahl der aequidistanten Punkten: "))
#Das Aufteilen der Schritte hat leider nicht geklappt

while x <= 0.5000:
    print("{} | {) | {:f}".format(x, sinx, Fehler))
    x = x+0.1111

