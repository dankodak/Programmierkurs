def pascal( N ):
    list=[1]
    for i in range(N):
        k=0
        print(list)
        newlist=[0] * (len(list)+1)
        newlist[k] = list[0]
        for j in range(len(list)-1):
            k=k+1
            newlist[k] = list[j]+list[j+1]
        newlist[k+1] = list[0]
        list=newlist
    return

pascal (10)