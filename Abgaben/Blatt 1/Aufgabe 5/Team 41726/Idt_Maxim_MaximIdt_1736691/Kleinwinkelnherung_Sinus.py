import math

print("Kleinwinkelnäherung vom Sinus")

x = float(input("Eingabe bis zum Wert 0.5: "))


while x <= 0.5:

    # Berechnung der Werte
    sin = math.sin(x)
    Fehler = abs(x - math.sin(x))
    
    
    print("{:2f} | {:3f} | {:.4f}".format(x, sin, Fehler))
    x = x + 0.1
    

input()                                          
