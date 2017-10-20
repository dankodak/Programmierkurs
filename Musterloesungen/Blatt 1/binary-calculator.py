# This program takes two integers and prints out the binary
# addition of the two numbers:

number1 = int(input("Zahl 1: "))
number2 = int(input("Zahl 2: "))

# Output of the numbers:
# Header:
result_binary = "{:b}".format(number1 + number2)
width_binary = len(result_binary)

# Output:
format_string = "{:>"+str(width_binary)+"b}"
print()
print("  " + format_string.format(number1))
print("+ " + format_string.format(number2))
print("-"*(width_binary + 2))
print("= " + format_string.format(number1+number2))
