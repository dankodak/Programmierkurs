# Berechnung der Summe aller Listenelemnte                             Emil Shirokikh

list1 = [1, 2, 3]
list2 = [1, [2, 3], [5, 7]]
list3 = [9, [9, [9, [9, 2], [2]]]]

def sum_list(L):
    sum=0
    for element in L:
        if isinstance(element, list):
            sum = sum + sum_list(element)
        else:
            sum = sum + element
    return sum
print (sum_list(list3))
