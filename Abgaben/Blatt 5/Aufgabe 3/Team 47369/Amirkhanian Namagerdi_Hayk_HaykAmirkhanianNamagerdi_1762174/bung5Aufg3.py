import math
from decimal import Decimal
def trapecoidal_rule(f,a,b,n):
    h = (b-a)/n
    I = 0
    for i in range(0,n):
        xi = a+i*h
        xi2 = a + (i+1) * h
        I = I + 0.5*h*(f(xi)+f(xi2))
    return I
def f(x):
    return x**2
def evaluate(f,a,b,n,G):
    print("n   |    approx.    |   error")
    for i in n:
        test = trapecoidal_rule(f,a,b,i)
        error = math.fabs(G-test)
        if i < 10:
            print ("{:.0f}   |   {:e}   |  {:.4f}".format(i,test,error))
        else:
            print("{:.0f}   |   {:e}  |  {:.4f}".format(i,test,error))
G = trapecoidal_rule
evaluate(f,0,1,[5,10],1/3)
# " 100% selbstgemacht"
