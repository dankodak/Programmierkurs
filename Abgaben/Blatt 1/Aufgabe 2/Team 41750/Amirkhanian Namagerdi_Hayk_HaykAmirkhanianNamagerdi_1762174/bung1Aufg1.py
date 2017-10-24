import cmath

a = int(input ("Erste Variable: "))
b = int(input ("Zweite Variable: "))
c = int(input ("Dritte Variable: "))          # Die 3 Variablen werden durch den Benutzer definiert
d = cmath.sqrt((b*b)-(4*a*c))                 # Die Diskriminante wird berechnet
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)                             # Die beiden Lösungen der Mitternachtsgleichung werden berechnet
print (x1)
print (x2)                                    # Die Lösungen werden ausgegeben







