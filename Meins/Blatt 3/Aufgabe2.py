def pascal(n):
    if n == 1:
        return [1]
    if n== 2:
        return [1,1]
    else:
        p = pascal(n-1)
        retlist = [1]
        for i in range(n-2):
            retlist.append(p[i] + p[i+1])
        retlist.append(1)
        return retlist
print(pascal(10))