#Euklidischer Algorithmus                   Emil Shirokikh

def euklidischer_algorrithmus(a, b):
    while b > 0:                          # b darf nicht Null sein da man auf keinen Fall durch Null teilen darf!
        a, b = b, a % b                    # ggT wird mit modulo definiert
    return a

a = int(input("Geben Sie a ein:"))
b = int(input("Geben Sie b ein:"))
print(euklidischer_algorrithmus(a, b))