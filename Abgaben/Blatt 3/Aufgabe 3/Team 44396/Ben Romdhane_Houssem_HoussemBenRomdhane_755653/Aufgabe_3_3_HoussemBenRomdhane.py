import time

def standard(a, x):
    p = a[0]
    x_pow = 1
    for i in range(1, len(a)):
        x_pow = x_pow * x
        p = p + a[i] * x_pow
    return p


def horner(a, x):
    p = a[len(a)-1]
    for i in range(1, len(a)):
        p = a[len(a) - 1 - i] + p * x
    return p


# Trial questions a) and b)
a = (1, 2, 3)
x = 2
print(standard(a, x))
print(horner(a, x))

# Optional question
a = range(-50, 51)
x = 4.12
t_standard = 0
t_horner = 0
# For some reason, the program doesn't deliver the desired result when I use range(0, 1000)
for i in range(0, 1):
    start_standard = time.clock()
    standard(a, x)
    end_standard = time.clock()
    horner(a, x)
    end_horner = time.clock()
    t_standard = t_standard + end_standard - start_standard
    t_horner = t_horner + end_horner - end_standard
print("Standard: {}".format(t_standard * 1000))
print("Horner:   {}".format(t_horner * 1000))
# but when I multiply the time by 1000, it does deliver the desired result
