a = 1
b = 1

input_right = False

while not input_right:
    a = int(input("Geben sie eine natuerliche Zahl A ein: "))
    print(a>0)
    print(a%a is 0)
    print(a is 0)
    if ((a > 0) and (a % a is 0)) or (a is 0):
        input_right = True
    else:
        print("Geben sie diesmal eine natuerliche Zahl fuer A ein:")

input_right = False

while not input_right:
    b = int(input("Geben sie eine natuerliche Zahl B ein: "))
    print(b%b)
    if ((b > 0) and (b % b is 0)) or (b is 0):
        input_right = True
    else:
        print("Geben sie diesmal eine natuerliche Zahl fuer B ein:")


    def ggT(a, b):

        if a is 0 or b is 0:
            return 0

        else:
            while (b is not 0):
                if a > b:
                    a = a - b

                else:
                    b = b - a

        return a

print(ggT(a, b))

