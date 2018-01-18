#Aufgabe3       Emil Shirokikh

#a)b)
import math
#from decimal import decimal

def trapecoidal_rule(f, a, b, n):
    h = float((b-a)/n)
    I = 0
    for i in range(n):
        I= f(a+i*h) + f(a+((i+1)*h))
    I= I *1/2* h
    return I


def evaluate(f, a, b, n, I):
    print(" n | approx. | error")
    for i in n :
        test = trapecoidal_rule(f,a,b,i)
        error = math.fabs(I -test)
        if i < 10 :
            print("{:.0f}   | {:e}  |   {:.4f}   ".format(i, test, error))
        else:
            print(" {:.0f}    | {:e}    | {:.4f}".format(i, test,error))


def f_1(x):
    y = 2 * x + 1
    return y


def f_2(x):
    y = x ** 2
    return y


def f_3(x):
    y = 3 / 2 * (math.sin(x)) ** 3
    return y


# evaluate(f_1,0,1,[5,10], 1/3)

n_default = [5, 10, 50, 100]

evaluate(f_1, 0, 1, n_default, 2)
evaluate(f_2, 0, 1, n_default, 1 / 3)
evaluate(f_3, 0, math.pi, n_default, 2)
evaluate(math.cos, 0, 2 * math.pi, n_default, 0)