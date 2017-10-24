import cmath
print("\nSolver for a quadratic equation:\n")
a = float(input("Enter coefficient {}: ".format("a")))
b = float(input("Enter coefficient {}: ".format("b")))
c = float(input("Enter coefficient {}: ".format("c")))
delta =  b ** 2 - (4 * a * c)
x1 = (b + cmath.sqrt(delta))/(2*a)
x2 = (b - cmath.sqrt(delta))/(2*a)
print('\nThe solutions for the quadratic equation are: {} and {}'.format(x1, x2))