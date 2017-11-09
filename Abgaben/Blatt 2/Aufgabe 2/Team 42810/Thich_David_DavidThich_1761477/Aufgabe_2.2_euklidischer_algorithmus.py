print("This program will calculate the greatest common divisor of your two natural numbers :)")

# zwei natürliche Zahlen werden eingegeben
a = int(input("Please enter your first natural number: "))
b = int(input("Plesae enter your seconds natural number: "))

# falls a oder b kleiner 0, also keine natürliche Zahl
if (a or b) < 0:
    print("The number you entered was below 0 :/\nTry Again :)")
    quit()

# falls a gleich 0, ist ggT gleich b, da jede Zahl die 0 teilt
elif a == 0:
    print("ggT({},{})=".format(a,b),b)
    quit()
# falls b gleich 0, ist ggT gleich a, da jede Zahl die 0 teilt
elif b == 0:
    print("ggT({},{})=".format(a,b),a)
    quit()

# falls a und b > 0, wird der Algorithmus ausgeführt
else:

    remainder_1 = max(a,b) % min(a,b)

# falls a gleich b, ist ggT gleich 1 und Programm muss stoppen, sonst Division durch 0
    if remainder_1 == 0:
        print("ggT({},{})=".format(a,b),1)
        quit()

    else:
        remainder_2 = min(a,b) % remainder_1

while remainder_2 != 0:

    remainder_1 = remainder_1 % remainder_2

    if remainder_1 == 0:
      print("ggT({},{})=".format(a,b),remainder_2)
      quit()

    else:
      remainder_2 = remainder_2 % remainder_1

print("ggT({},{})=".format(a,b),remainder_1)

# ich weiß das Programm ist etwas zu lang, aber bei Spezialfällen würde sonst eine Division durch 0 erfolgen