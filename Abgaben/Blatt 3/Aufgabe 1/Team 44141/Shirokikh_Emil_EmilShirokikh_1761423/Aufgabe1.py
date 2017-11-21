# Kurzform der Mengen- und Listenoperationen in Python                    Emil Shirokikh

# a.
# Werte Selber auswaehlen, wobei a der Anfang und B das Ende des Intervalls ist.
a = 3
b = 6
n = 4

deltaX = (b - a) / n
seq = []

for i in range(0, n + 1):
    seq.append(a + i * deltaX)

print(seq)

#b.

N = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Teiler ={(a,b)for a in N for b in N if a%b ==0 }
print(Teiler)


#c.
Pythagoras ={(a,b,c)for a in N for b in N for c in N if a*a + b*b == c*c}
print(Pythagoras)


