import math

x = (-0.5)
q = 1
n = int(input("Die Anzahl der Schritte: "))   # Variablen werden definiert und die Anzahl der Schritte wird eingelesen
c = "x"
d = "sin(x)"
e = "Fehler"
print ("      {:2}   |  {:3}   | {:.6}".format(c,d,e))  # Die Kopfzeile der Tabelle wird erstellt
while q <= (n):                               # Es soll n Schritte geben
    a = math.sin(x)
    b = math.fabs(a-x)
    q = q + 1                                 # Die Anzahl der Schleifendurchläufe werden hiermit kontrolliert
    print("{:2f}  | {:3f} | {:.4f}".format(x, a, b))   # Die Ergebnisse werden in Tabellenform widergegeben
    x = x + ((0.5)-(-0.5))/(n - 1)            # X wird um den Wert der in der Aufgabe im Hinweis stand erhöht
