a = 10
b = 60
n = 50
i = 1
List = []
while i <= n:
    deltax = (b-a)/n
    x = a + i*deltax
    List.append(x)
    List.append(i)
    List.append(deltax)
    i = i + 1
    print(List)
    List = []


