def list_sum(L):
    result = 0
    for i in range(len(L)):
        if isinstance(L[i],int):
            result = result + L[i]
        elif isinstance(L[i],list):
            if len(L[i])!= 0 :
                b = L[i]
                result = result + list_sum(b)
    return result

print(list_sum([1,2,3]))
print(list_sum([1,[2,3],[5,7]]))
print(list_sum([9,[9,[9,[9,2],[2]]]]))
