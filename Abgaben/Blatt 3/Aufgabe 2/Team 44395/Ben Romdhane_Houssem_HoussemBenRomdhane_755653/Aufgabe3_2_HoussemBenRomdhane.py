def pascal(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        var = pascal(n-1)
        my_list = [1]
        for i in range(0, n-2):
            my_list.extend([var[i] + var[i+1]])
        my_list.extend([1])
        return my_list


x = pascal(10)
print(x)
