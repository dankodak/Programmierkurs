import math


def trapecoidal_rule(f, a, b, n=100):
    intgrl = 0
    h = (b-a)/n
    for i in range(0, n):
        intgrl += .5 * h * (f(a+i*h)+f(a+(i+1)*h))
    return intgrl


def evaluate(f, a, b, n, I):
    print("{:4}".format("n"), "|", "{:11}".format("approx."), "|", "{:11}".format("error"))
    for i in n:
        intgrl = trapecoidal_rule(f, a, b, i)
        print("{:4}".format(i), "|", "{:11.4e}".format(intgrl), "|", "{:11.4e}".format(abs(intgrl-I)))
    pass


def f_1(x):
    return 2 * x + 1


def f_2(x):
    return x*x


def f_3(x):
    return 1.5 * (math.sin(x))**3


def f_4(x):
    return math.cos(x)


evaluate(f_1, 0, 1, [5, 10, 50, 100], 2)
print("\n")
evaluate(f_2, 0, 1, [5, 10, 50, 100], 1/3)
print("\n")
evaluate(f_3, 0, math.pi, [5, 10, 50, 100], 2)
print("\n")
evaluate(f_4, 0, 2*math.pi, [5, 10, 50, 100], 0)
print("\n")
