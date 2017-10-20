import math
import numpy as np

n=input("n: ")
interval = np.linspace(-0.5,0.5,n)
print("{:^10}|{:^10}|{:^10}".format("x","sin(x)","Fehler"))
for i in interval:
    print("{:^10.4f}|{:^10.4f}|{:^10.4f}".format(i,math.sin(i),math.fabs(i-math.sin(i))))