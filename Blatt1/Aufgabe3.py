number1 = input("Erste Zahl: ")
number2 = input("Zweite Zahl: ")
width = 9
print(" {:>{width}b}".format(number1,width = width))
print("+{:>{width}b}".format(number2,width = width))
print("-"*10)
print("={:>{width}b}".format(number1+number2,width = width))
