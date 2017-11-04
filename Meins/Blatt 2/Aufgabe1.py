import math

n = float(input("Anzahl Messdaten:"))
if n == int(n):
    n = int(n)
while type(n) != int or n<=0:
    n = float(input("Eingabe falsch, wiederholen:"))
    if n == int(n):
        n = int(n)

data = []
for i in range(n):
    data.append(float(input("Datenpunkt eingeben: ")))

#Mittel
Mittel = sum(data)/n
print(Mittel)

#Varianz
Var = 0
for i in range(n):
    Var += (data[i] - Mittel)**2
Var = Var/n
print(Var)

#Abweichung
s = (math.sqrt(Var))
print(s)