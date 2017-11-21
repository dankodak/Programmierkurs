# Sieb des Eratosthenes

def eratosthenes(n):
    n_sqrt = int(round(n**(1/2)+0.5))
    B = {a*b for a in range(2,n_sqrt+1) for b in range(2,int(round(n/a))+1)}
    N = {x for x in range(2,n+1)} - B
    return N
    
n = 100
print(eratosthenes(n))