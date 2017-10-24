import math
x = -0.5
print ("bitte geben sie die Zahl der gewünschten äquidestanten Punkte an")
n = int(input())
print("   X    ","|","sin(x)  ","|","     fehler")
while x <= 0.5 :
    fehler = math.fabs(math.sin(x)-x)
    print(repr(round(x ,4)).rjust(8) , "|" ,repr(round(math.sin(x) ,4)).rjust(8) , "|" ,repr(round(fehler ,4)).rjust(8))
    x = x + 1/(n-1)

