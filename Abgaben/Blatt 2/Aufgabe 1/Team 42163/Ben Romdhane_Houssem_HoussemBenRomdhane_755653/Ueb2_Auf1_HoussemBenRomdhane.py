import numpy as np
import math
print("\nStatistical Analysis of Measurement Data: \n")
n = int(input("Enter number of elements as a positive number: "))
good_to_go = n > 0
while not good_to_go:
    n = int(input("The number you entered is not a positive integer, try again: "))
    good_to_go = n > 0
print("")
i = 0
measurements_list = []
while i < n:
    new_entry = float(input("Enter element number "+ str(i+1) +" : "))
    measurements_list.append(new_entry)
    i = i + 1

print("\nArithmetic average = {}\nVariance = {} \nStandard deviation = {}".format(np.mean(measurements_list), np.var(measurements_list), math.sqrt(np.var(measurements_list))))
#These methods were used in lecture 1, page 6



