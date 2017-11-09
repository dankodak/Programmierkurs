import math
input_correct = False
while not input_correct:
    z = int(input("Positive ganze zahl eingeben: "))
    if z >= 1:
        input_correct = True
    else:
        print("Bitte nochmal probieren.")

L1 = []
L2 = []
i = 1
while i <= z:
    xi = float(input("werte eingeben: "))
    L1.append(xi)
    i = i + 1
print("eingegebene Werte: " ,L1)

AM = sum(L1)/z
print("arithmetisches mittel=", AM)

i = 0
while i <= z-1:
    d = (L1[i]*AM)**2
    L2.append(d)
    i = i + 1
print("Liste 2" ,L2)
V2 = sum(L2)/z
print("Varianz=", V2)

s = math.sqrt(V2)
print("Standardabweichung=", s)
print("arithmetisches mittel={:.4f} Varianz={:.4f} Standardabweichung={:.4f}".format(AM ,V2 ,s))