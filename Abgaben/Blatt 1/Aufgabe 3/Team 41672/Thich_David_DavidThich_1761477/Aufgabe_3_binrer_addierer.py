print ("This programm will add two decimal number in binary form")

# zu berechnende Zahlen werden eingegeben
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your seconds number: "))

# Umformung in Binärschreibweise
binary_number_1 = "{:b}".format(number_1)
binary_number_2 = "{:b}".format(number_2)

# Länge der Binärzahlen
length_b1 = len(str(binary_number_1))
length_b2 = len(str(binary_number_2))

# Ergebnis der Addition der beiden Zahlen in Binärschreibweise
result = "{:b}".format(number_1+number_2)
# Länge der Zahl in Binärschreibweise
length_result = len(str(result))

print("Zahl 1:",number_1)
print("Zahl 2:",number_2)
print(" ")

print(" "*(length_result-length_b1+2) + binary_number_1)
print("+"," "*(length_result-length_b2) + binary_number_2)

print("-"*(length_result+2))

print("=",result)