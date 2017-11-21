#Question a: The interval's limits can either be defined by the user
# or entered directly in the code

#Alternative 1:
#a = float(input("Enter interval lower bound: "))
#b = float(input("Enter interval upper bound: "))
#n = int(input("Enter the number of steps: "))
#Alternative 2: Will be used in this question to be able to directly
# access the sets from questions b) and c)
a = 1
b = 21.5
n = 50

set_a = [a + i*(b-a) / n for i in range(0, n+1)]
print(set_a)

#Question b:
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = [(x, y) for x in A for y in A if x%y == 0]
print(set_b)

#Question c:
set_c = [(c1, c2, c3) for c1 in A for c2 in A for c3 in A if (c1**2 + c2**2 == c3**2)]
print(set_c)