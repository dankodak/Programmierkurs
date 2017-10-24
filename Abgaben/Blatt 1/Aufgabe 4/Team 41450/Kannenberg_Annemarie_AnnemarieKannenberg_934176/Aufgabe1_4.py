print("Computes n factorial")
n = int(input("n="))
i=n
n_factorial=1
while i>0:
    n_factorial = n_factorial*i
    i=i-1
	
print("n!="+str(n_factorial))
