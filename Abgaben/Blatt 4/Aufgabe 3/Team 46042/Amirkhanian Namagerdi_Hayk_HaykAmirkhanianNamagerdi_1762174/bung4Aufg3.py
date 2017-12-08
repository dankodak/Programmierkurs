B=[1,[2,3],[5,7]]
def list_sum(L):
    sum = 0
    for element in L:
        if isinstance(element, list):
            sum = sum + list_sum(element)
        else:
            sum = sum + element
    return sum
print(list_sum(B))