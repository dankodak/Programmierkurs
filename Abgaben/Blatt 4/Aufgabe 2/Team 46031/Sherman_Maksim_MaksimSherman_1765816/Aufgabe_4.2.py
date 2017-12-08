
from math import sin, pi
import math


def heaviside(x):
    if x < 0:
        return 0
    else:
        return 1


def smoothed_heaviside(x, epsilon=1e-3):
    if x< -epsilon:
        return 0

    elif -epsilon <= x <= epsilon:
        w = 1/2 + x/(2*epsilon)+ (1/(2*(pi)))* (sin(((pi*x)/epsilon)))
        return w

    else:
        return 1


def get_piecewise_polynomial(p, a):

    def g(x):

        for i in range(0, len(p) - 1):
            if p[i] <= x < p[i + 1]:
                return a[i]
        else:
            return 0
    return g

