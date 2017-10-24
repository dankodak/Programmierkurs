import cmath

print ("This program will solve your quadratic equation :)\nax**2 + bx + c")

# Koeffizienten a, b und c werden eingegeben
a = float(input("Enter a number (unequal 0) for a please: "))
b = float(input("Enter a number for b please: "))
c = float(input("Enter a number for c please: "))

# Diskriminante und Wurzel davon werden berechnet
discriminant = b**2 - 4*a*c
value_of_discriminant = cmath.sqrt(discriminant)

# Mitternachtsformel
x1 = (-b + value_of_discriminant) / (2*a)
x2 = (-b - value_of_discriminant) / (2*a)
x0 = -b / (2*a)

# falls Diskriminante > 0: 2 Lösungen
if discriminant > 0:
                    print ("This equation has two solutions: x1= {:.3f}, {:.3f}".format(x1,x2))

# falls Diskriminante = 0: genau eine Lösung
elif discriminant == 0:
                    print ("This equation has only one solution: x= {:.3f}".format(x0))

# falls Diskriminante < 0: 2 komplexe Lösungen
elif discriminant < 0:
                    print ("This equation has two complex solutions: x1= {:.3f}, x2= {:.3f}".format(x1,x2))