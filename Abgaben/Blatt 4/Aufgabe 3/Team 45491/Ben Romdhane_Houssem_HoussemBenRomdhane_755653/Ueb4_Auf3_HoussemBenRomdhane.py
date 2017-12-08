def list_sum(l):
    my_sum = 0
    for i in range(0, len(l)):
        if isinstance(l[i], list):
            my_sum = my_sum + list_sum(l[i])
        else:
            my_sum = my_sum + l[i]
    return my_sum


A = [1, 2, 3]
B = [1, [2, 3], [5, 7]]
C = [9, [9, [9, [9, 2], [2]]]]
print(list_sum(A))
print(list_sum(B))
print(list_sum(C))