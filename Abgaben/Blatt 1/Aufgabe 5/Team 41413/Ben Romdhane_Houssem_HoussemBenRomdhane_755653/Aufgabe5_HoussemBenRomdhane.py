import math
number_steps = int(input("Bitte Anzahl der Schritte eingeben: "))
print("{:^7}".format("x"), "|", "{:^7}".format("sin(x)"), "|", "{:^7}".format("Fehler"))
i = 0
while i < number_steps:
    x = -0.5 + (i/(number_steps-1))
    print("{:7.4f}".format(x),"|", "{:7.4f}".format(math.sin(x)), "|", "{:7.4f}".format(math.fabs(x-math.sin(x))))
    i = i + 1
