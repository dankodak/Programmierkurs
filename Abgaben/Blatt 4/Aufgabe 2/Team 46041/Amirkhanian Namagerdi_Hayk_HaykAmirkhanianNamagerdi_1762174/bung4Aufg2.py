from math import fabs

# BITTE IMPLEMENTIEREN SIE IHRE FUNKTIONEN
# HIER. ÄNDERN SIE NICHT DEN UNTEREN PROGRAMMTEIL.
import math
def heaviside(x):
    if x < 0:
        y = 0
        return y
    if x >= 0:
        y = 1
        return y
def smoothed_heaviside(x, epsilon=1e-3):
    if x < ((-1) * epsilon):
        y = 0
        return y
    if ((-1) * epsilon) <= x <= epsilon:
        y = 0,5 + (x/(2*epsilon)) + (1/(2*math.pi)*math.sin((math.pi * x)/epsilon))
        return y
    if x > epsilon:
        y = 1
        return y
a = [1,2,3]
p = [-1, 1, 2, 2.5]
def get_piecewise_polynomial(p,a):
    def getFun(x):
        if p[0] > x or p[len(p)-1] < x:
                              return 0
        else:
            for i,p_i in enumerate(p):
                if p_i <= x and x < p[i+1]:
                    return a[i]
    return getFun



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
