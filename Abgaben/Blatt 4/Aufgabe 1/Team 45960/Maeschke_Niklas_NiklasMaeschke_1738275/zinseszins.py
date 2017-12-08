from interest import aktuelles_guthaben
a = 0
jahre=0
print (aktuelles_guthaben(1000,3600,0.1))

while a<1:
    jahre=jahre+1
    if (aktuelles_guthaben(1000,360*jahre,0.1) >= 2000):
        a=1
print (jahre)

