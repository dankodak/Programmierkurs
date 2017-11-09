#Monte Carlos pi-Näherung                             Emil Shirokikh

from random import random

n = int(input("Gesamtzahl der zufällig verteilten Punkte "))
p = 0
x=0; y = 0
for i in range(1, n+1):
    x = random()
    y = random()
    if x * x + y * y <= 1:
        p = p + 1
pi_approx = 4.0 * p / n
print ("pi ist ca.",pi_approx)