# Fakultät berechnen                           Emil Shirokikh

def fakul(n):   # Wir definieren was die Fakultät einer beliebigen Zahl n >= 1 ist
    summe = 1
    i = 1
    while (i < n + 1):              # Wir multiplizieren immer die erste Zahl 1 mit der darauffolgenden Zahl bis wir
        summe = summe * i           # unsere Zahl n erreichen ( also quasi 1 * (1+1) * (1+1+1) *....* n )
        i = i + 1
        print(summe)

zahl = input("Folgende Fakultät soll berechnet werden: ")
zahl = int(zahl)                # unsere Zahl ist keine Dezimalzahl
fakul(zahl)                     # Der Befehl fakul(n) soll ausgeführt werden

