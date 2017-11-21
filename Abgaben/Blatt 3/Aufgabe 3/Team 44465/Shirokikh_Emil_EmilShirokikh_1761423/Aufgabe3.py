import time

# Horners Schema                       Emil Shirokikh

#b.
def horner(a, x):
    p = 0
    for c in reversed(a):
        p = p * x + c
    return p


print(horner((1, 2, 3), 2))

#a. horners sheme

def standart(a, x):
    p = 0
    xi = 1
    for c in a:
        p += c * xi
        xi*=x
    return p
print(standart([1,2,3],2))

#c. horners sheme

def standart(a, x):
    p = 0
    xi = 1
    for c in a:
        p += c * xi
        xi*=x
    return p
print(standart([1,2,3],2))
a = range(-50, 50)
start = time.clock()
for i in range(10000):
    standart(a, 4.12)
end = time.clock()
print("Die Funktion Standart benötigt:{:.3e} s" .format(end - start ))

a =  range(-50,50)
start1 = time.clock()
for k in range(10000):
    horner(a, 4.12)
end1 = time.clock()
print("Die Funktion Horner benötigt:{:.3e} s " .format(end1 - start1))