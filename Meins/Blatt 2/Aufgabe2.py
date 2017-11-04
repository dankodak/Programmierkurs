a = int(input("a"))
b = int(input("b"))

if a == 0:
    ggT = 0
else:
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    ggT = a
print(a)