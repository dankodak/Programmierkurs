#Kleinwinkelnäherung                                 Emil Shirokikh

from math import fabs
from math import sin

x = -0.5
print(" Enter äquidistante Zahl: ")
n = int(input())

print(" x        |   sin(x)    |     Fehler  ")  #Ausgabeform wird erstellt

import math

while x <= 0.5:
    Fehler = math.fabs(math.sin(x) - x)                           # Definition von 'Fehler'
    print((repr(round(x, 4)).rjust(8), "|", repr(round(math.sin(x), 4)).rjust(8), "|", repr(round(Fehler, 4)).rjust(8)))
    x = x + 1 / (n - 1)
    # Aufteilung des Bereichs -0.5 bis 0.5 in gleichmäßige Schritte und Berechnung der jewiligen Werte der Tabelle
