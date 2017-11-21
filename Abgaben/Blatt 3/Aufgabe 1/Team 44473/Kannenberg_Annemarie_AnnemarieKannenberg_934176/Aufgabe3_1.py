import math as m
import numpy
# Aufgabe 1a)
# lower and upper bound
a, b = 1,10
#number of Elements in list
n=20
#generate list with n lements 
A = numpy.linspace(a,b,num=n)
print('A =',A)

#Aufgabe 1b)
Y = {1,2,3,4,5,6,7,8,9,10}

B = {(x,y) for x in Y for y in Y if (x/y).is_integer()}
print('B =',B)

#Aufgabe 1c)
Z = {1,2,3,4,5,6,7,8,9,10}


C = {(s,t,r) for s in Z for t in Z for r in Z if s**2 + t**2 == r**2}

print('C =',C)