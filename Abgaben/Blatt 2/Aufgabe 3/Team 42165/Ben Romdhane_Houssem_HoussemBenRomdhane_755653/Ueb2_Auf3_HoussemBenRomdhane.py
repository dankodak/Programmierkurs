import math
print("\nPi-Approximation:\n")
N = int(input("Enter N: "))
list_a, list_b, list_c = [], [], []
i = 0
while i <= N:
    list_a.append(4 * ((-1)**i) / (1+2*i))
    list_b.append(2 * ((-1)**i) * (3**(.5-i)) / (1+2*i))
    list_c.append((1/(16**i))*((4/(1+8*i)) - (2/(4+8*i)) - (1/(5+8*i)) - (1/(6+8*i))))
    i = i + 1

print("\n   N | Fehler a) | Fehler b) | Fehler c)")
i = 1
while i <= N:
    error_a = abs(math.fsum(list_a[:i]) - math.pi)
    error_b = abs(math.fsum(list_b[:i]) - math.pi)
    error_c = abs(math.fsum(list_c[:i]) - math.pi)
    print("{:4}".format(i), "|", "{:9.2e}".format(error_a),"|","{:9.2e}".format(error_b),"|","{:9.2e}".format(error_c))
    i = i + 1
