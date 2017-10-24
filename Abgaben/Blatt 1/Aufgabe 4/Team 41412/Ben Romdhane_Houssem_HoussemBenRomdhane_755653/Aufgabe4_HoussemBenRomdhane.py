number = int(input("Enter natural number n: "))
factorial = 1
i = 1
while i <= number:
    factorial = factorial * i
    i = i + 1
print("n!=", factorial)