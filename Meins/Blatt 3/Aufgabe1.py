a = 1
b = 2
n = 10
delta = (b-a)/n
linspace = [a + i * delta for i in range(n)]
print(linspace)

tupel = [(a,b) for a in range(1,11) for b in range(1,11) if a%b == 0]
print(tupel)

pyth = [(a,b,c) for a in range(1,11) for b in range(1,11) for c in range(1,11) if a**2 +b**2 == c**2]
print(pyth)