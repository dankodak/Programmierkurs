import math
a = int(input("natuerliche zahl: "))
b = int(input("natuerliche zahl: "))
#Der Algorithmus funktioniert nur bei natuerlichen zahlen

if (a==0):
    print('ggT(a,b)=')
elif a > b:
    while b != 0:
        a, b = b, a%b

    print('Der ggT={}'.format(a))

else:
    while a != 0:
        b, a = a, b%a
    print('der ggT={}'.format(b))
