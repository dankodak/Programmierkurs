print("\nCalculate the Greatest Common Divisor of two Integers: \n")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
x, y = a, b
if a == 0:
    gcd = 0 #I didn't know that 0 could be considered as a divisor,
            #the logic behind this if statement from the pseudo-algorithm is unclear
else:
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    gcd = a

print("\ngcd("+ str(x)+ ", "+ str(y)+") = " +str(gcd))

