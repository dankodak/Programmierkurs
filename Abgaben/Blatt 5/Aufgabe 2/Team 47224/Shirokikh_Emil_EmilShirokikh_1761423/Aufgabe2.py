# Aufgabe2         Emil Shirokikh

# a)b)c)

class Polynomial():
    def __init__(self, *a):  # <3
        self._coefficient = list(a)

    def __call__(self, x):
        p = 0
        for i in range(len(self._coefficient)):
            p = p + self._coefficient[i] * x ** i
        return p

    def __str__(self):
        ret = ""
        for i in range(len(self._coefficient)):
            if self._coefficient[i] != 0:
                if i == 0:
                    ret = ret + str(self._coefficient[i])
                else:
                    ret = ret + str(self._coefficient[i]) + "*x^" + str(i)
                if i != len(self._coefficient) - 1:
                    ret = ret + " + "

        return ret


pol = Polynomial(1, 2, 3)
polizei = Polynomial(4, 3, 2, 1)
print(pol(2))
print(pol.__call__(2))
l = [1, 2, 3]
print(l)
print(polizei)

