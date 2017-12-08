import sys
import interest

for i in sys.path:
    print(i)

print(interest.gesamt(10000,0.1,3600))

n=1
while interest.gesamt(10000, 0.1, n) < 20000:
    n +=1

print(n/360)