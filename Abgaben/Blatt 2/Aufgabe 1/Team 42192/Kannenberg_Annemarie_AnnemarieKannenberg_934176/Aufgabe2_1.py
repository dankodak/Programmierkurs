import math
# computes mean, variance and standard deviation from a set of data points

# INPUTS: 	n 	- number of data points; must be positive integer
#			x_i - data point

# OUTPUTS: 	mean - arithmetic mean from data
#			var	 - variance from data	
#			dev  - standard deviation from data

#read in number of data points
n = float(input ("number of data points n = "))

# determine wether number of data points n is a positive integer
# if not read new n
while not(n.is_integer() and n>=0):
    print("n must be positive integer")
    n = float(input("number of data points n = "))


#define variables	
x = []
x_var  = []
i = 0

# read  data points
while i<=(n-1):
    x[i:i] = [float(input("x_"+str(i+1)+"="))]
    i = i+1

# compute mean	
mean = (1/n) * sum(x)

i=0
# compute variance	
for x_i in x:
	x_var[i:i] = [(x_i - mean)**2]
	i = i+1
	
var = (1/n)* sum(x_var)

# compute standard deviation
dev = var**(1/2)

print("mean = " + str(mean))
print("variance = " + str(var))
print("standard deviation = " + str(dev))

