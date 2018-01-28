def mm(A,B):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    C = []
    for d in range (len(A)):
        for a in range (len(A)):
            for b in range (len(A)):
                e = e + A[a][b] * B[c][d] + A[a][b+1]*B[c+1][d]
                c = c + 1
            C.append(e)
    return C
print (mm([[1,2],[3,4]],[[1,2],[3,4]]))
