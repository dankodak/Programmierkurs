import math
def interest(prozent,a0,n):
    #a0=1000
    #prozent=0.1
    #n=1000
    a=a0*(1+prozent/(36000))**n
    print(a)
    return a
def jahr(persent,a,a0):
    n=(math.log(a/a0)/math.log(1+(persent/36000)))/360
    print(n)
    return n
interest (0.1,1000,3600)
jahr(0.1,2000,1000)