import math


def eratosthenes(n):
    set_n = set([i for i in range(2, n+1)])
    set_b = set([k * i for k in range(2, 1+int(math.ceil(n**.5))) for i in range(2, 1+int(math.ceil(n/k)))])

    return set_n - set_b


print(eratosthenes(20))


