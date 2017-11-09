a=int(input("a="))
b=int(input("b="))
if (a==0 or b==0):
    print("ggt=0")
else:
    while a!=b:
        if a>b:
            a=a-b

        else:
            b=b-a

print("ggT=",a)