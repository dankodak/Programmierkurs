print("Fakultät berechnen")

Benutzerzahl = int(input("Bitte Zahl eingeben: "))

#7! = 7*6*5*4*3*2*1

fak = 1

while Benutzerzahl > 0:
    fak = fak * Benutzerzahl
    Benutzerzahl = Benutzerzahl - 1

print(fak)

input()
