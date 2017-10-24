x = 1
f = 1
n = int(input("Die Zahl: "))        # Variablen und die Zahl derer Fakultät berechnet werden soll wird definiert
while x <= (n-1):                   # Die Definition für die Schleife wird definiert
    d = f * n
    f = d * 1                       # Das Zwischenergebnis wird hiermit zwischengespeichert, damit es beim nächsten
    n = n - 1                       # Durchgang nicht verloren geht, wobei die Schleife (n/1)-1 mal wiederholt wird
print("Die Fakultät der Zahl lautet:" + str(f))    # Das Endergebnis wird als String ausgedrückt

