print ("This programm will calculate the faculty of your number")

# zu berechnende Fakultät einer Zahl wird eingegeben
n = int(input("Enter a natural number: "))
Result = 1

while (n-1) > 0:

# Anfangswert 1 wird mit n multipliziert
    Result = Result * n
# danach wird n um 1 verringert
    n = n-1

print("The faculty of your number is:",Result)

# falls 0 eingegeben wird, wird 1 ausgegeben, da 0! = 1
if n == 0:
    print (1)