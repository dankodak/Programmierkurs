#Pascalsches Dreieck      Emil Shirokikh

liste = [[1]]
liste2 = []
zähler = 0

zeilen = int(input("So viele Zeilen soll es geben: "))

while zähler != zeilen:
    for i in range(zeilen - 1):
        for j in range(len(liste[i]) + 1):
            if j >= 1 and j <= len(liste[i]) - 1:
                zahl = liste[i][j - 1] + liste[i][j]
                liste2.append(zahl)
            else:
                liste2.append(1)

        if liste2 not in liste:
            liste.append(liste2)

        liste2 = []

    zähler += 1

grösstes_element = len(str(max(liste[-1])))
letzte_zeile = ' '.join([str(eintrag).center(grösstes_element) for eintrag in liste[-1]])

for i in liste:
    print(' '.join([str(eintrag).center(grösstes_element) for eintrag in i]).center(len(letzte_zeile)))
