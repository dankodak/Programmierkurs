print("Lösen einer quadratischen Funktion der Form ax**2 + b*x + c = 0")

import math


print("Koeffizienteneingabe:")

a = int(input("Bitte Wert für a eingeben: "))

b = int(input("Bitte Wert für b eingeben: "))

c = int(input("Bitte Wert für c eingeben: "))

# Berechnung der Diskriminante
d = (b**2) - (4*a*c)
if (d < 0):
    print("Es gibt kein Ergebnis.")
elif (d == 0):
    print("x ="), (-b)/(2*a)
elif (a == 0):
    print("Es gibt kein Ergebnis.")
else:
    print("Nullstellen")
input()
Lösung1 = (-b-math.sqrt(d))/(2*a)
Lösung2 = (-b+math.sqrt(d))/(2*a)

print(Lösung1, Lösung2)


input()
