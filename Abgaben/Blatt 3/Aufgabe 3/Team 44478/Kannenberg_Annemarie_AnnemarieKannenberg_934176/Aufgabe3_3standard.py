#Aufgabe 3a)
# funktion für klassische berechnung des wertes p(x)
import time


def standard(a,x):
    n = len(a)
    p=0
    for i in range(0,n):
        p = p+a[i]*x**i
    return p


a = [1,2,3,4,5,6]
x = 2
N = 1000
start = time.clock()
for i in range(N):
    p = standard (a,x)
end = time.clock()
time = end - start

time_standard = time/N

print(('Gesamtzeit:{} Sek.\n'+"Ein Schleifendurchlauf: {}Sek.").format(time, time_standard))

print(p)