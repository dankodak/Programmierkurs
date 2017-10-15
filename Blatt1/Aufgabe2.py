import cmath

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("x1= " , (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a))
print("x2= " , (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a))