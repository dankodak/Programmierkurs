from cmath import sqrt

a = float(input('Wert fuer a: '))
b = float(input('Wert fuer b: '))
c = float(input('Wert fuer c: '))

x1 = (- b + sqrt((b * b) - (4 * a * c))) / (2 * a)
x2 = (- b - sqrt((b * b) - (4 * a * c))) / (2 * a)

print('x1 =', x1, 'und x2 =', x2)
