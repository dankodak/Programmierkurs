import math
a = range(-0.5,0.5,0.1)
for i in range(-0.5,0.5,0.1):
    sinx = math.sin(i)
    sin  = round(sinx,4)
    approx = math.fabs(sin - i)
    approxi= round(approx,4)
    print("   x","|"," sin(x)","|","Fehler")
    print(i,"|",sin,"|",approxi)