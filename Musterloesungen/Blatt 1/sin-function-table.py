import math

n = int(input("Bitte Anzahl der Schritte eingeben:"))
a = -.5
b = 0.5
dx = (b-a) / (n-1)

i = 0
while i < n:
    x0 = a + i*dx
    sinx = math.sin(x0)
    print("{:7.4f} | {:7.4f} | {:8.6f}".format(x0, sinx, math.fabs(sinx - x0)))
    i = i + 1
