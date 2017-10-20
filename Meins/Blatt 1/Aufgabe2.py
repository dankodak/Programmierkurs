import cmath

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("x1= " , (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a))
print("x2= " , (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a))