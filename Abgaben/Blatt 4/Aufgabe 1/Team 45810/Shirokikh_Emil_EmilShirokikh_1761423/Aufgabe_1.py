#Zinsberechnung                 Emil Shirokikh

import math
from math import log
from math import e

def A(A0, p, n):
    if A0>=0:
        result_principal = A0*((1+(p/(360*100)))**n)
        return result_principal
    elif A0<0:
        return (" Blöd gelaufen.")

def A0(A, p, n):
    A0 = (A/(1 + (p/360*100))**(-1*n))
    return A0

def n(A0, A, p):
    n =(log(A/A0,e))/(log(1+ (p/(360*100)),e))
    n_in_years = n/360
    return n_in_years

def p(A0, A, n):
    p = 360*100 *((A/A0)**(1/n)- 1)
    return p

print(" The resultive principal is about : " + str(A(1000, 0.1, 360*100)))
print(" It will take you this many years to double your principal: " + str(n(1000, 50000, 0.1)))