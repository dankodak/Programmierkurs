summand1 = int(input("Zahl 1: "))
summand2 = int(input("Zahl 2: "))
length_summand1 = len(str("{:b}".format(summand1)))
length_summand2 = len(str("{:b}".format(summand2)))
length_binary_sum = len(str("{:b}".format(summand1+summand2)))
print()
print(" "*(length_binary_sum-length_summand1+2)+str("{:b}".format(summand1)))
print("+ "+" "*(length_binary_sum-length_summand2)+str("{:b}".format(summand2)))
print("-"*(length_binary_sum+2))
print("= "+str("{:b}".format(summand1+summand2)))


