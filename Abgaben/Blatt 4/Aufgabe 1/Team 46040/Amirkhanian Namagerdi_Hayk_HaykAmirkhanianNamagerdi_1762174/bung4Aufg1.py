import math
import cmath                                               #Kei
def A(A0,p,n):
    if A0 < 0:
        return ("Das afg")
    if A0 >= 0:
        Endguthaben = A0*((1+(p/36000))**n)
        return Endguthaben
def A0(A, p, n):
    Anfangsguthaben =  (A / (1 + (p / 36000)) ** (-n))
    return Anfangsguthaben
def n(A0, A, p):
    Tageszahl =  math.log((A/A0),math.e)/math.log((1+(p/(360*100))),math.e)
    Jahreszahl = Tageszahl / 360
    return Jahreszahl
def p(A0, A, n):
    Zinssatz = (36000 * ((A / A0) ** (1 / n) - 1))
    return Zinssatz
print ("Das Endguthaben beträgt:" + str(A(1000, 0.1 , 36000)))
print ("Die Anzahl der Jahre beträgt:" + str(n(1000 , 2000 , 0.1)))

#Keiner konnte mir sagen wie man das Modul richtig abspeichert da das nur mit jupyter file vorgezeigt wurde.


