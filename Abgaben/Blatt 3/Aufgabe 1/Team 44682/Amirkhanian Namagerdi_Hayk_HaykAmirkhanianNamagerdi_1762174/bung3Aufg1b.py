import math
N = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
B = [(i,j) for i in N for j in N if (i/j) in N]
print(B)