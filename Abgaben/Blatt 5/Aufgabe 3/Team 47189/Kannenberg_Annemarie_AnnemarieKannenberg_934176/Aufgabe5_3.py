import math

#Aufgabe 3 (a)

def trapecoidal_rule(f,a,b, n=100):
#aproximation of Integral of a function f with trapecoidal rule
#Inputs: f - function
#        a - lower bound for integration
#        b - upper bound for integration
#        n - number of steps for aproximation

#Outputs: I = approximation of Integral
    I = 0
    for i in range(n):
        h = abs(b-a)/n
        x = a+i*h
        x_plus = a+(i+1)*h
        I = I + 1/2 *h* (f(x) + f(x_plus))
    
    return I
    
    
# Aufgabe 3(b)
    
def evaluate(f,a,b,n,I):
# evaluates aproximation of Integral with trapecoidal_rule for different numbers of steps n_default
# and prints table with aproximation of integral and error
#Inputs: f - function
#        a - lower bound for integration
#        b - upper bound for integration
#        n - list of different numbers of steps for the aproximation
#        I - value of Integral if known
#Outputs: In = approximation of Integral    
    print("{:^3}".format('n')+"|"+"{:^10}".format('approx')+"|"+"{:^10}".format('error'))
    for n_i in n:
        I_n = trapecoidal_rule(f,a,b,n_i)
        print("{:^3d}".format(n_i)+"|"+"{:^10.3e}".format(I_n)+"|"+"{:^10.3e}".format(abs(I-I_n)))
    return I_n


I = trapecoidal_rule(math.sin,0,2*math.pi)  

#print(I)
#evaluate(math.sin,0,2*math.pi, [5,10,15,20],0)

def f_1(x):
    y =2*x+1
    return y

def f_2(x):
    y = x**2
    return y
    
def f_3(x):
    y =3/2*(math.sin(x))**3
    return y

#evaluate(f_1,0,1,[5,10], 1/3)

n_default = [5, 10, 50, 100]


evaluate(f_1,0,1,n_default,2)
evaluate(f_2,0,1,n_default,1/3)
evaluate(f_3,0,math.pi,n_default,2)
evaluate(math.cos,0,2*math.pi,n_default,0)