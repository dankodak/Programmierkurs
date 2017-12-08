from math import fabs


# BITTE IMPLEMENTIEREN SIE IHRE FUNKTIONEN
# HIER. ÄNDERN SIE NICHT DEN UNTEREN PROGRAMMTEIL.

import math # sonst gibts probleme bei der smoothed_heaviside letzten assert Abfrage
from math import pi
from math import sin
# Heaviside Funktion     Emil Shirokikh

# a. heaviside Funktion

def heaviside(x):
    if x < 0:
        res = 0
    else:
        res = 1
    return res


# b. smoothed_heaviside Funktion

def smoothed_heaviside(x, epsi=10 ** (-3)):  # ich weiß dass es nicht sehr schön ist
    if x < -1 * epsi:
        res = 0
        return res
    elif x > epsi:
        res = 1
        return res
    elif -1 * epsi <= x <= epsi:
        res = 0.5 + (x / (2 * epsi)) + (sin((pi * x) / epsi) / (2 * pi))
        return res




# c.




def get_piecewise_polynomial(p, a):
    def retFun(x):

        if p[0] > x or p[len(p) - 1] < x:
            return 0
        else:
            for i, p_i in enumerate(p):
                if p_i <= x and x < p[i + 1]:
                    return a[i]

    return retFun


####################################################################
"""
Bitte den folgenden Teil des Programms nicht mehr editieren:
Hier werden Ihre Funktionen automatisch getestet.

Der assert Befehl erwartet True als Argument, andernfalls wird die
Ausführung des Programms mit einer Fehlermeldung abgebrochen.
"""
assert heaviside(1) == 1
assert heaviside(-1) == 0
assert heaviside(0) == 1
print("a) OK")

assert smoothed_heaviside(-1) == 0
assert smoothed_heaviside(1) == 1
assert smoothed_heaviside(-1e-4) > 0
assert smoothed_heaviside(-1, 2) > 0
assert fabs(smoothed_heaviside(1, 2) - (0.5 + 0.25 + 1 / 2 / math.pi)) < 1e-10
print("b) OK")

a = [1, 2, 3]
p = [-1, 1, 2, 2.5]
polynomial = get_piecewise_polynomial(p, a)
assert polynomial(-10) == 0
assert polynomial(10) == 0
assert polynomial(-1) == 1
assert polynomial(0) == 1
assert polynomial(1) == 2
assert polynomial(2.25) == 3
print("c) OK")

print("Es scheint alles korrekt zu sein! Sehr gut!")
