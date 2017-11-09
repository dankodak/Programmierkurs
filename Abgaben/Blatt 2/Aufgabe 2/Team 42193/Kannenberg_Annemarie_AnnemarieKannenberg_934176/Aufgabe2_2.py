## Euklidscher Algorithmus

# determine greatest common divisor (gcd) from two positive integers a, b

print("algorithm to determine greatest common divisor (gcd) from to positive integers")

# read in integers
a,b = float(input("int1=")), float(input("int2="))

# euklidean algorithm
if a==0:
    gcd = 0
else:
    while b!=0:
        if a>b:
            a = a-b
			
        else:
            b = b-a

    gcd = a

# write out gcd	
print("gcd=" + str(gcd))

