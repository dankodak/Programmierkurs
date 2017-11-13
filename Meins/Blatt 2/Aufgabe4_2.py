import random
import math
import numpy as np

n = 10000
counter = 0
for i in range(n):
    x = random.random()
    y = random.random()
    if x**2 + y**2 < 1:
        counter += 1

approx = 4 * counter/n
print(approx)
print(math.fabs(math.pi - approx))