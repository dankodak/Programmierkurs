from math import fabs

# BITTE IMPLEMENTIEREN SIE IHRE FUNKTIONEN
# HIER. ÄNDERN SIE NICHT DEN UNTEREN PROGRAMMTEIL.

import math


def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1


def smoothed_heaviside(x, epsilon=1e-3):
    if x < -epsilon:
        return 0
    elif x > epsilon:
        return 1
    else:
        return .5 + .5 * (x/epsilon) + (.5/math.pi) * math.sin((math.pi * x / epsilon))


def get_piecewise_polynomial(p_f, a_f):
    def g(x):
        pol = 0
        i = 0
        while i < len(a_f) and pol == 0:
            if p_f[i] <= x < p_f[i+1]:
                pol = a_f[i]
            i = i + 1
        return pol
    return g



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
assert fabs(smoothed_heaviside(1, 2) - (0.5 + 0.25 + 1/2/math.pi)) < 1e-10
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
