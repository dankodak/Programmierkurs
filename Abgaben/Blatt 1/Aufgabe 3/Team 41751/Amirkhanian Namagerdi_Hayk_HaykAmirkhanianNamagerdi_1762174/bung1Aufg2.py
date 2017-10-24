Zahl1 = int(input("Die erste Zahl lautet: "))
Zahl2 =int(input("Die zweite Zahl lautet: "))                    # Die Zahlen die addiert werden sollen werden definiert
Ergebnis = Zahl1 + Zahl2                                         # Das Ergebnis wird berechnet
print("Zahl1:" +" {:>9b}".format(Zahl1))                         # Die Zahlen die addiert werden, werden zur besseren
print("Zahl2:" + " {:>9b}".format(Zahl2))                        # Übersicht nochmal dargestellt
print(" {:>9b}".format(Zahl1))
print("+{:>9b}".format(Zahl2))
print("-"*15)                                                    # Die Rechnung wird so wie in der Aufgabe dargestellt
print("=" + "{:>15b}".format(Ergebnis))                          # erzeugt
print (str("Das Ergebnis dieser Addition beträgt in Binärschreibweise {:b}".format(Ergebnis))) # Das Ergebnis wird
# als String in der Binärschreibweise widergegeben
# Ich habe keinen Ansatz gefunden um die Länge der Ausgabe des Ergebnis in binärer Darstellung dynamisch darzustellen