from math import log

def gesamt(a0, p, n):
    return a0*(1 + p/36000)**n

def anfang(a, p, n):
    return a*(1 + p(36000))**(-n)

def anzahl(a0, a, p):
    return log(a/a0)/log(1+p/36000)

def zins(a0, a, n):
    return 36000*((a/a0)**(1/n)-1)