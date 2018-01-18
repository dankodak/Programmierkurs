import numpy as np

while True:
    try:
        n = int(input("Please enter a natural number for n: "))
        break
    except:
        print("The number entered wasn't a natural number!")

a = []
b = []

for i in range(1,n*n+1):
    a.append([i])
    b.append([i])

# A und B sind quadratische Matrizen mit Einträgen [1,2,3,...,n*n]
A = np.array(a)
A = A.reshape(n,n)

B = np.array(b)
B = B.reshape(n,n)

[I,J] = A.shape

[K,H] = B.shape

C = np.zeros((I,H))

for i in range(I):
    for j in range(H):
        for k in range(K):

            C[i,j] = C[i,j] + A[i,k]*B[k,j]

print(C)

