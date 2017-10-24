import math
print ("bitte erste zahl eingeben")
a = int(input())
print ("bitte zweite zahl eingeben")
b = int(input())
print(" {:>9b}".format(a))
print("+{:>9b}".format(b))
print("_"*(6+len(bin(a+b))))
print(" {:>9b}".format(a+b))

