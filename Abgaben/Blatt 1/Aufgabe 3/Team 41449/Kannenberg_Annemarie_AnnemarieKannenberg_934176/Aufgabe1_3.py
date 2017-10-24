print("Compute sum of two integers with binary output")

number1 = int(input("Int1 = "))
number2 = int(input("Int2 = "))
length = len("={:>b}".format(number1+number2))
space = "{:>"+str(length)+"b}"
space_plus1 = "{:>"+str(length+1)+"b}"
print(space_plus1.format(number1))
print("+"+space.format(number2))
print("-"*(length+1)) 
print("="+space.format(number1+number2))