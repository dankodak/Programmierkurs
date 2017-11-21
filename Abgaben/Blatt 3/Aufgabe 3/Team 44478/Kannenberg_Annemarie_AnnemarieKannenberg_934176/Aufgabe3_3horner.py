#Aufgabe 3b)
# # Horner-Schema
import time
def horner(a,x):
    n=len(a)
    p = 0
    for i in range(0,n-1):
        p = (p+a[n-1-i])*x
    p = p + a[0]
    return p

a = [1,2,3,4,5,6]
x = 2
N = 1000

start = time.clock()
for i in range(N):
    p = horner (a,x)
end = time.clock()
time = end - start

time_standard = time/N

print(('Gesamtzeit:{} Sek.\n'+"Ein Schleifendurchlauf: {}Sek.").format(time, time_standard))