#Solving quadratic equation                                            Emil Shirokikh

from cmath import sqrt

a = int(input("enter first coefficient: "))    # enter three coefficients a,b and c
b = int(input("enter second coefficient: "))
c = int(input("enter third coefficient:"))

disc = b**2 - 4*a*c                            # Sei disc die Diskriminante
                                               # Die Lösung der quadratischen Gleichungen seien x1 und x2
                                               # Fallunterscheidung in drei Fälle

                                               # Im Fall 1 ist die disc streng größer Null
if disc > 0:
  x1 = (-b - sqrt(disc))/(2*a)
  x2 = (-b + sqrt(disc))/(2*a)

  print('x1 =',x1,'; x2 =',x2)

elif disc == 0:                                # Im Fall 2 ist disc gleich Null
  x1 = (-b)/(2*a)
  print ('x =',x1)

elif disc < 0:
    print("Jetzt haben wir eine negative Diskriminante und eine komplexe Lösung!")

else:
    print("something went terribly wrong")
