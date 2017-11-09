#Arithmetisches Mittel                           #Emil Shirokikh

def durchschnitt(zahlen):
    return float(sum(zahlen))/max(len(zahlen),1)        #Die Einzelnen Elemnte werden summiert und durch deren Anzahl
                                                        # geteilt
print(durchschnitt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Varianz
from statistics import variance
zahlen = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(variance(zahlen))

#Standartabweichung
from math import sqrt                                  #Die Standartabweichung ist definiert als Wurzel der Varianz

sigma = sqrt(variance(zahlen))
print(sigma)
