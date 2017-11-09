import math
from decimal import Decimal

def format_e(n):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]

print ("bitte groesstes n eingeben")
groesstes_n = int(input())


n=0

print(repr("N").rjust(8), "|", repr("Fehler a").rjust(25), "|", repr("Fehler b").rjust(25),"|", repr("Fehler c").rjust(25))
while n<=groesstes_n:
    pi_summands_a = [1] * (groesstes_n + 1)
    pi_summands_b = [1] * (groesstes_n + 1)
    pi_summands_c = [1] * (groesstes_n + 1)
    pi_approx_a = 0
    pi_approx_b = 0
    pi_approx_c = 0
    pi_error_a = 0
    pi_error_b = 0
    pi_error_c = 0
    i = 0
    while i <= n:
        pi_summands_a[i] =(4*(-1)**i)/(2*i+1)
        pi_summands_b[i] =((2*(-1)**i)*3**(0.5-i)/(2*i+1))
        pi_summands_c[i] =(1/(16**i))*((4/(8*i+1))-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6)))
        i =i+1

    i=0
    while i <= n:
        pi_approx_a =pi_approx_a + pi_summands_a[i]
        pi_approx_b = pi_approx_b + pi_summands_b[i]
        pi_approx_c = pi_approx_c + pi_summands_c[i]
        i=i+1

    pi_error_a = math.fabs(math.pi-pi_approx_a)
    pi_error_b = math.fabs(math.pi-pi_approx_b)
    pi_error_c = math.fabs(math.pi-pi_approx_c)


    print(repr(n).rjust(8), "|", (format_e(Decimal(repr(pi_error_a)))).rjust(25), "|", (format_e(Decimal(repr(pi_error_b)))).rjust(25),"|", (format_e(Decimal(repr(pi_error_c)))).rjust(25))
    n= n+1
