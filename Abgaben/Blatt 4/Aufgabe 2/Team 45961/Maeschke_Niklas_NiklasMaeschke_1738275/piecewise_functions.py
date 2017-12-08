from math import fabs
import math


# BITTE IMPLEMENTIEREN SIE IHRE FUNKTIONEN
# HIER. ÄNDERN SIE NICHT DEN UNTEREN PROGRAMMTEIL.


def heaviside(x):
    b = 1
    if x < 0 :
        b = 0
    return b


def smoothed_heaviside(x, epsilon=1e-3):
    b = 0
    if -epsilon <= x <= epsilon:
        b = 0.5 + (x / 2 / epsilon) + (1 / 2 / math.pi) * math.sin(math.pi * x / epsilon)
    elif x > 0:
        b = 1
    return b

def get_piecewise_polynomial(p, a):
    def g(x):
        n=1
        b=0
        while n<len(p):
            if p[n-1]<= x <p[n]:
                b=a[n-1]
            n=n+1
        return b
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
assert smoothed_heaviside(-1,2) > 0
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