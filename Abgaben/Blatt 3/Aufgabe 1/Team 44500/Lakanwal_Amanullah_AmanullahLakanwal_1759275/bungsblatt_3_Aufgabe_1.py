import math
a=float(input("Beliebigen Wert a für Intervall eingeben:"))
b=float(input("Beliebigen Wert b für Intervall eingeben:"))
n=int(input("Anzahl der Schritte eingeben:"))

ixi = []
ideltax=[]

i=0
while i <= n:
    xi=i*((b-a)/n)+a
    ixi.append(xi)
    i=i+1
    print(ixi)

N={1,2,3,4,5,6,7,8,9,10}
Z={(a,b)for a in N for b in N if a/b==0}

print(Z)

y={(a,b,c)for a in N for b in N for c in N if((a**2)+(b**2)==(c**2)
    print(y)
