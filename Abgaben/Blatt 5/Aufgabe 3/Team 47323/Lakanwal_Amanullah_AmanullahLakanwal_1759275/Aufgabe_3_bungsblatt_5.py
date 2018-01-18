import math

def trapecoidal_rule (f, a, b, n=100) :
    I=0
    h=(b-a)/n
    for i in range (n):
        I+=(1/2)*h*(f(a+i*h)+f(a+i+1)*h)
    return I

def evaluate(f, a, b, n, I= None):
    if I != None:
        print("{:>3}|\t{:<10}|\t{:<10}".format("n","approx.","ERROR"))
        for i in range(len(n)):
            print("{:>3}|\t{:<10.3e}|\t{:<10.3e}".format(n[i],trapecoidal_rule(f, a, b, n=n[i]), math.fabs(trapecoidal_rule(f,a,b,n=n[i])-I)))
        else:
            print("{:>3}|\t{:<10}".format("n","approx."))
            for i in range (len(n)):
                print("{:>3}|\t{:<10.3e}".format(n[i]),trapecoidal_rule(f,a,b,n=n[i]))
    pass


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