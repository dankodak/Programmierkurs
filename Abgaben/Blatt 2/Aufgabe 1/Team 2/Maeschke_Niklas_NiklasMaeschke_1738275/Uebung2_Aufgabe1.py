import cmath
input_right = False
data_list = []
while not input_right:
    n = int(input("Geben sie die Anzahl der Messdaten ein: "))
    if n >= 0:
        input_right = True
    else:
        print("Die Anzahl der Messdaten war ungueltig. Bitte geben sie sie erneut ein!: ")

list_done = False
counter = n
while not list_done:
    print("Geben sie den",counter,".-ten Messwert ein:")

    data_list.insert(counter, float(input()))
    counter = counter-1
    
    if counter is not 0:
        list_done = False
    else:
        list_done = True
        
arithmetic_average = 0
for i in range(0,n):
    arithmetic_average = arithmetic_average+data_list[i]

arithmetic_average = arithmetic_average/n
print("Das Arithmetische Mittel betraegt: ",arithmetic_average)

variance = 0
for l in range(0,n):
    variance = variance+((data_list[l]-arithmetic_average)**2)

variance = variance / n
print("Die Varianz betraegt:", variance)

standard_deviation = cmath.sqrt(variance)
print("Die Standardabweichung betraegt:", standard_deviation)

