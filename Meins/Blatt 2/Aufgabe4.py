import random
import math
import numpy as np

n = 1000

points = [(random.random(), random.random()) for i in range(n)]

counter = 0
for i in range(n):
    if np.linalg.norm(points[i]) < 1:
        counter += 1

approx = 4 * counter/n
print(approx)
print(math.pi - approx)