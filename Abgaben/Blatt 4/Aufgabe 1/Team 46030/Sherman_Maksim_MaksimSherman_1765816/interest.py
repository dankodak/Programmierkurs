import math


def verzinsung(A0, p, n):

    A = A0*(1+ (p/(360*100)))**n
    return A

def anfangsbetrag(A, p, n):

    A0 = A*part(p)**(-n)
    return A0

def anzahl_tage(A0, A, p):

    n = (math.log(A/A0))/(math.log(part(p)))
    return n

def zinseszins(A0, A, n):

    p = 360*100*((A/A0)**(1/n)-1)
    return p

def part(p):
    part = 1+ (p/(360*100))
    return part
