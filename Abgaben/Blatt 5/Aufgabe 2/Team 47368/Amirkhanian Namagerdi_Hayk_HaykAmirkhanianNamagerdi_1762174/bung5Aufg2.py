class Polynomial:
    def __init__(self,*factors):
        global cf
        cf = factors
    def __str__(self):
       i = 0
       list = []
       for i in range (len(cf)):
            if cf[i] > 0:
             a = str(cf[i])
             list.append(a+"*x^"+str(i))
       string = "+".join(list)
       return string
    def __call__(self,x):
        Potenz = 0
        Summe = 0
        for i in cf:
            Summe = Summe + i * x**Potenz
            Potenz = Potenz + 1
        return Summe
c1 = Polynomial(1,0,4)
print (c1)
#So eine Dreckaufgabe hahhahah
# Nicht mal mehr witzig hahaha