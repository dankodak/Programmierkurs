print("Addition in Binärdarstellung")

Zahl1 = int(input("Gib eine Zahl ein: "))
Zahl2 = int(input("Gib eine Zahl ein: "))

print(" {:>9b}".format(Zahl1))
print(" +{:>9b}".format(Zahl2))
print("-"*10)
print("={:>9b}".format(Zahl1+Zahl2))

input()


