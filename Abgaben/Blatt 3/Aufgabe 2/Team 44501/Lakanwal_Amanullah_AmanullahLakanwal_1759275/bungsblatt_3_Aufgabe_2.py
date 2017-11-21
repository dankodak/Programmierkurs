import math
def pascal (n):
if n ==1:
return [1]
else:
zeile =[1]
vorherige_zeile =pascal(n-1)
for i in range(len(vorherige_zeile)-1):
    zeile.append(vorherige_zeile[i]+vorherige_zeile[i+1])
    zeile + =[1]
return zeile

print(pascal(1))
