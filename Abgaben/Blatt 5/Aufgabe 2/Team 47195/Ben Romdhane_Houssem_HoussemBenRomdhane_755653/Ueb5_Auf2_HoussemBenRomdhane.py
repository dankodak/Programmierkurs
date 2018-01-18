class Polynomial:
    def __init__(self, *coeffs):
        self.coefficients = list(coeffs)

    def __call__(self, x):
        pol = 0
        for i in range(len(self.coefficients)):
            pol = pol + self.coefficients[i]*x**i
        return pol

    def __str__(self):
        pol = ""
        for i in range(0, len(self.coefficients)):
            if self.coefficients[i] != 0:
                if pol != "":
                    pol = pol + " + "
                pol = pol + str(self.coefficients[i]) + " * x^" + str(i)
        return pol


p = Polynomial(0, 2, 5, 8, 1, 2, 3)
print(p)
print(p(1))
