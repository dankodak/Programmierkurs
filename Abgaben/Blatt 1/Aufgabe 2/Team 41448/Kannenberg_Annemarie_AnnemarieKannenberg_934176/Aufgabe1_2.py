import cmath
print("solver for second-order-polynominal equation of type ax²+bx+c")
a, b, c = float(input("a=")), float(input("b=")), float(input("c="))

x_1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
x_2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)

print("Solution to the equation is given by x_1 =" + str(x_1) + "and x_2 =" + str(x_2))



