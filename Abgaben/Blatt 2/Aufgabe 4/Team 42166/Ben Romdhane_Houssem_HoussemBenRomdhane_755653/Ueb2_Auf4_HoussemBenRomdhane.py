import random
import math
print("\nMonte-Carlo Approximation of Pi: \n")
n = int(input("Enter the desired number of draws: "))
p = 0
for i in range(1, n+1):
    x, y = random.random(), random.random()
    if (x**2)+(y**2) <= 1:
        p = p + 1

print("\nMonte-Carlo approximation: {}".format(4*p/n))
print("Error = {:.2e}".format(abs((4*p/n)-math.pi)))
print("Error in % = {:4.2f}%".format(100*(abs((4*p/n)-math.pi))/math.pi))
