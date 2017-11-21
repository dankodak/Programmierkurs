list1=[i for i in range(1,11)]
list2=[i for i in range(1,11)]
print(list1, list2)
for j in range (1,10):
    for i in range(1,10):
        if (list1[j]%list2[i]==0):
            print(list1[j],list2[i])
            i+=i
    j+=j

