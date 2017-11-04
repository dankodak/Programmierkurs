import math
N = int(input("N:"))

list1 = [4 * ((-1)**i)/(2*i+1) for i in range(N)]
list2 = [(2*(-1)**i * 3**(1/2 - i))/(2*i+1) for i in range(N)]
list3 = [1/(16**i)*(4/(8*i+1)-2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6)) for i in range(N)]

pi1 = 0
pi2 = 0
pi3 = 0

print("{:^5}|{:^10}|{:^10}|{:^10}".format("N","a","b","c"))
for i in range(N):
    pi1 += list1[i]
    pi2 += list2[i]
    pi3 += list3[i]
    print("{:^5}|{:^10.4f}|{:^10.4f}|{:^10.4f}".format(i, math.fabs(math.pi - pi1), math.fabs(math.pi - pi2), math.fabs(math.pi - pi3)))