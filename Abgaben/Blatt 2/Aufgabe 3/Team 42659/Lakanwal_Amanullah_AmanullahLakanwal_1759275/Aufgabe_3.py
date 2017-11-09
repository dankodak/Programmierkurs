import math
print("Berechnung der Näherungsweise Pi")
z=int(input("Wie viele Schritte sollen ausgeführt werden?"))
print("N | Fehler a) | Fehler b) | Fehler | c)")

list1=list()
list2=list()
list3=list()

i=0

#Fehlerspalte 1
while i<z:

    si= 4*(-1)**i/(2*i+1)
    list1.insert(0,si)
    Beispiel1=sum(list1)
    Fehler1=math.fabs(math.pi-Beispiel1)

    #Fehlerspalte 2
    si2= (2*(-1)**i*3**0.5-i)/(2*i+1)
    list2.insert(0,si2)
    Beispiel2=sum(list2)
    pi=math.pi
    Fehler2=math.fabs(pi-Beispiel2)

#Fehlerspalte 3
    si3=(1/(16**i))*((4/(8*i+1))-(2/8*i+4))-(1/(8*i+5))-(1/(8*i+6))
    list3.insert(0,si3)
    Beispiel3=sum(list3)
    Fehler3=math.fabs(math.pi-Beispiel3)
    i=i+1
    print("{:2} |   {:.2e}  |   {:.2e}  |   {:.2e}".format(i,Fehler1, Fehler2, Fehler3))
