#Monte Carlo Approximation

import random as rand
import math

# read number of random values

n = int(input("number of random values n = "))

p = 0
# create data random data points
for i in range(1,n):
    x = rand.random()
    y = rand.random()
    z = x**2+y**2
	# check if data points are in unit circle
    if z <= 1:
       p = p+1

# compute approximation of pi and uncertainty
pi = 4*p/n
uncert = math.fabs(math.pi - pi)
	
# write approximation and uncertainty	
print("approximated pi =" + str(pi) + " with uncertainty of " + str(uncert))
