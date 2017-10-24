#Zahlen als Binärcodes addieren                             Emil Shirokikh

a = int(input("Zahl 1: "))      # Wir wandeln die zu addierende  Zahlen  a und b in Binärcodes um
b = int(input("Zahl 2: "))

print("{:>9b}".format(a))      # mit den folgenden 4 Schritten soll die die Abbildung wie auf dem Aufgabenblatt entstehen
print("+ {:>9b}".format(b))
print("-"*15)
print("={:>9b}".format(a+b))   # Erst jetzt findet die Addition der zwei Zaheln a und b binär statt

