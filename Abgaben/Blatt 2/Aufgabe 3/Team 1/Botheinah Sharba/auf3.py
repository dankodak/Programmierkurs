import math
n=int(input("n="))
if n==0:
    print(" zero is not acceptable")
else :
    s=0
    s1=0
    s2=0

    for i in range (0,n):
        a=4*((-1)**i)/(2*i+1)
        b=(2*(-1)**i)*3**(1/(2-i))/(2*i+1)
        c=(1/16**i)*(((4/(8*i+1))-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6))))
        s=s+a
        s1=s1+b
        s2=s2+c
print("{:4s} |{:8s} | {:8s} | {:8s}".format("n","fehler a","fehler b","fehler c"))
print("{:4f} |{:8f} | {:8f} | {:.8f}".format(n,abs(s-math.pi),abs(s1-math.pi),abs(s2-math.pi)))



