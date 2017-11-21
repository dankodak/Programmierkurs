def pascal(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1 , 1]
    if n != 1 or 2:
        x = 0
        Ergebnis = [1]
        p = pascal(n-1)
        while x <= (n-3):
            Ergebnis.append(p[x]+p[x+1])
            x = x + 1
        Ergebnis.append(1)
        return Ergebnis
print(pascal(10))

