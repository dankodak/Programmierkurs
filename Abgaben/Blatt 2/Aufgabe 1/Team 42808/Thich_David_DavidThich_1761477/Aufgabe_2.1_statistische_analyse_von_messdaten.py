import math

print("Dieses Programm wird Ihnen das Arithmetische Mittlel, die Varianz und die Standardabweichung Ihres Wertes berechnen :)")

# es wird angegeben, wie viele Messwerte vorliegen
n = int(input("Please enter natural number unequal 0: "))

# falls n keine positive Zahl bzw. 0 ist
if n <= 0:
    print("The number you entered was 0 or below!\nPlease try again.")
    quit()

result_1 = 0
result_2 = 0
result_3 = 0

# angefangen wird bei 1, Länge der Schleife gleich n+1, d.h es wird n-mal aufsummiert
for i in range(1,n+1):

    x_i = i
    result_1 = result_1 + x_i

arithmetisches_mittel = result_1 * 1/n

for i in range(1,n+1):

    x_i = (i - arithmetisches_mittel) ** 2
    result_2 = result_2 + x_i

varianz = result_2 * 1/n

standardabweichung = math.sqrt(varianz)

print("Arithmetisches Mittel =",arithmetisches_mittel)
print("Varianz = {:.5}".format(varianz))
print("Standardabweichung = {:.5f}".format(standardabweichung))
