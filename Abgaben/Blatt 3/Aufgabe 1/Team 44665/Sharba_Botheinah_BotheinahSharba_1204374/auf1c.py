list1=[i for i in range(1,11)]
list2=[i for i in range(1,11)]
list3=[i for i in range(1,11)]
for a in range (1,10):
    for b in range(1, 10):
        for c in range(1, 10):
            if (list1[a]**2+list2[b]**2==list3[c]**2):
                print(list1[a],list2[b],list3[c])
                c+=c
        b+=b
    a+=a
