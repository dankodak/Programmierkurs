import cmath
a = int(input("a = ")); b = int(input("b = ")); c = int(input(" c = ")) # Wähle Werte für die Variablen a, b, c.
print("Die Lösung der quadratischen Gleichung", a , "x² + ",b,"x + ",c," = 0 ist:")
if a != 0:
    print("x_1 =" + str((-b + cmath.sqrt(b**2 - 4*a*c))/(a*2))+", x_2 ="+str((-b - cmath.sqrt(b**2 - 4*a*c))/(a*2)))
elif a == 0 and b != 0:
    print("x =" + str((-c)/b))
elif b == 0 and a != 0:
    print("x_1 =" + str(cmath.sqrt(-4*a*c)/2*a) + ", x_2 =" + str(-cmath.sqrt(-4*a*c)/2*a))
elif b == 0 and a == 0 and c != 0:
    print("Widerspruch")
elif b == 0 and a == 0 and c == 0:
    print ("x_1, x_2 beliebig")