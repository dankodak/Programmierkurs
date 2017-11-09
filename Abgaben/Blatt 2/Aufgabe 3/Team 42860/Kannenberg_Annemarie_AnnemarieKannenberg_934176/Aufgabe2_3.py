# computes 3 approximations of pi and uncertainty
import math as m

# number of itaritive steps
n = int(input("number of itaritive steps n for approximation n = "))

# define format strings for output table
nlen = str(len(str(n)))
format_string1 = "{:^"+nlen+"}|{:^12}|{:^12}|{:^12}"
format_string2 = "{:^"+nlen+"}|{:^10.6e}|{:^10.6e}|{:^10.6e}"

# define lists for 3 aproximations
a=[]
b=[]
c=[]

# compute summands for each approximation
i=0
while i <= n-1:
    a[i:i] = [(4*(-1)**i)/(2*i+1)]
    b[i:i] = [2*((-1)**i)*3**((1/2)-i)/(2*i+1)]
    c[i:i] = [1/16**i*(4/(8*i+1) - 2/(8*i+4)- 1/(8*i+5) - 1/(8*i+6))]
    i = i+1
	
print(format_string1.format("N","Fehler a", "Fehler b", "Fehler c"))

sum_x = 0
sum_y = 0
sum_z = 0
l = 0
# compute approximation-sums and write uncertainity in table
for x,y,z in zip(a,b,c):
    l = l+1
    sum_x = sum_x + x
    sum_y = sum_y + y
    sum_z = sum_z + z
    print(format_string2.format(l, m.fabs(sum_x-m.pi), m.fabs(sum_y-m.pi), m.fabs(sum_z-m.pi)))