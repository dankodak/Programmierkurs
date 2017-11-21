import math
A = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
B = [(a,b,c) for a in A for b in A for c in A if (a*a) + (b*b) is (c*c)]
print(B)
