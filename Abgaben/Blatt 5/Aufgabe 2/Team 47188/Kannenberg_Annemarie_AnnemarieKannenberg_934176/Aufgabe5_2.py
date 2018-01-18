class Polynomial(object):
    # Klasse für Polynome
    
    # definition eines Konstruktors der beliebige Koeffizienten eines Polynoms
    # übergeben bekommt
    # schreibt die Koeffizienten in eine Liste
    def __init__(self, *coeffs):
        self.coeffs = []
        for i in coeffs:
            self.coeffs.append(i)
        
        
    # Definition der Funktion zum auswerten des Polynoms an einer stelle x
    # mit x als eine beliebige reelle Zahl
    # Aufruf mit polynomname(x)
    def __call__(self, x):
        y = 0
        for a,i in zip(self.coeffs, range(len(self.coeffs))):
            y = y + a*x**i
        return y
        
# Funktion zur Bestimmung des Polynoms als Zeichenkette
# Gibt Polynom als Zeichenkette der Form a*x+b*x^2+... aus    
    def __str__(self):
        string = ""
        for a,i in zip(self.coeffs, range(len(self.coeffs))):                          
            if a != 0:
                if string != "":
                    string = string + "+"
                    
                if i == 0:
                    string = string + str(a)
                elif i == 1:
                    string = string + str(a) + "*x"  
                else:
                    string = string + str(a) + "*x^" + str(i)
        return string
    
p = Polynomial(1, 3, 3, 0, 2)

print(p.coeffs)
print(p(0))
print(p)


p1 = Polynomial(1, 0, 3)
print("p(0) =", p1(0))  # es sollte 1 erscheinen
print("p(1) =", p1(1))  # es sollte 4 erscheinen
print(p1) # es sollte die Ausgabe 1 + 3*x^2 erscheinen