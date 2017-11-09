import math

print("This program will calculate an approximation for π with 3 different formulas")

# Anzahl der Schritte für Näherung wird eingegeben
n = int(input("Please enter number of steps for the approximation: "))

print(" N |  Fehler_f1   |  Fehler_f2   |  Fehler_f3")
print("-"*45)

result_1 = 0
result_2 = 0
result_3 = 0

# angefangen wird bei 0, Länge gleich n
for i in range(0,n):

# Formeln
    f1 = 4 * ((-1) ** i) / (2 * i + 1)
    f2 = 2 * (-1) ** i * 3 ** (0.5 - i) / (2 * i + 1)
    f3 = (1 / 16 ** i) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))

# Summenformel
    result_1 = result_1 + f1
    result_2 = result_2 + f2
    result_3 = result_3 + f3

# Fehler bei der Annäherung
    error_1 = math.fabs(result_1-math.pi)
    error_2 = math.fabs(result_2-math.pi)
    error_3 = math.fabs(result_3-math.pi)

    print("{:>2} |  {:.3e}   |  {:.3e}   |  {:.3e}".format(i+1,error_1,error_2,error_3))