import math

n = int(input("Zahl n: "))
output = 1
while n > 0:
    output *= n
    n -= 1
print(output)