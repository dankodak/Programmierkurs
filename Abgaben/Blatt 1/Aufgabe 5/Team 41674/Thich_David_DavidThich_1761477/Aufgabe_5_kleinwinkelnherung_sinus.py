import math

print ("This program will show the small-angle approximation for sinus")

# Schritte für die Näherung wird eingegeben
steps = int(input("Please enter number of steps: "))

print ("   x    "+"|"+" sin(x) "+ "|" +"  error  ")
print ("-"*25)

# man fängt von -0.5 an
x = -0.5
# die Differenz zwischen den einzelnen Schritten
difference = 1/(steps-1)

while x <= 0.5:

    sin = math.sin(x)
    error = math.fabs(x) - math.fabs(sin)

    print ("{:>7.4f} |{:>7.4f} |{:>7.4f}".format(x,sin,error))

# man tut in gleich großen Schritten dazu addieren
    x = x + difference