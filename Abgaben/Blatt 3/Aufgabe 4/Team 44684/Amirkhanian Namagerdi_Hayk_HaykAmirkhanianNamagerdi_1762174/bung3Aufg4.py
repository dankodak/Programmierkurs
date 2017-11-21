import math
nmax = int(input("Die Zahl bis zu der die Primzahlen angegeben werden sollen angeben: "))
def erasthotenes(nmax):
    G = {s for s in range(2, nmax)}
    Prim = {a for a in G for b in G  for c in G if a/b == c}
    return (G - Prim)
print(erasthotenes(nmax))
