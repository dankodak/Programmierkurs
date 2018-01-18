def mm(A,B):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    C = [[0,0],[0,0]]
    for g in range (len(A)):
        for f in range(len(A)):
            e = 0
            for b in range (len(A)):
                e = e + A[g][b] * B[b][f]
            C[g][f] = e
            a = a + 1
        d=d+1
    return C
print(mm([[1,2],[3,4]],[[1,2],[3,4]]))