#import math
n=int(input("please enter a positive number n="))
sequence = [i for i in range(1,n+1)]
print("list=",sequence)

sum_x=sum(sequence)
arth=sum_x/n
print("Arithmetisches Mittel=",arth)

new_list = [(x-arth)**2 for x in sequence]
#print("list2=",new_list)
Varianz=sum(new_list)/n
print ("Varianz=", Varianz)
Standardabweichung= Varianz**0.5
print("Standardabweichung=",Standardabweichung)