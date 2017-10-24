print("numeric computation of sinus, small-angle approximation and uncertainty in n iterative steps")
import math
n = int(input("chose number of steps: n="))
a=-0.5
b=0.5
interval = (b-a)/(n-1)

print("{:^10}".format("x")+"|"+"{:^10}".format("sin(x)")+"|"+"{:^10}".format("uncertainty"))


while a<=b:
   sinus = math.sin(a)
   uncertainty = math.fabs(sinus-a)
   print("{:>10.4f}".format(a)+"|"+"{:>10.4f}".format(sinus)+"|"+"{:>10.4f}".format(uncertainty))
   a=a+interval
