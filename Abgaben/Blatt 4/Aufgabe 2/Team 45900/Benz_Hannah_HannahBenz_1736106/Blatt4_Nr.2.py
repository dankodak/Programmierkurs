
# coding: utf-8

# In[52]:


#a)
def heaviside(x):
    if x<0:
        return 0
    else:
        return 1
heaviside(-1)


# In[61]:


#b)
from math import sin
from math import pi
import math
def smoothed_heaviside(x, epsilon=1e-3):

    if x< -epsilon:
        return 0
    if -epsilon<=x<= epsilon:
        return (1/2 +(x/(2*epsilon))+1/(2*pi)*sin((pi*x)/epsilon))
    if x> epsilon:
        return 1
smoothed_heaviside(8,2)


# In[64]:


#c)
def get_piecewise_polynomial(p, a):
    def piecewise_polynomial(x):
        n=len(p)
        
        if x<p[0] or x>p[n-1]:
            return 0
        else: 
            i=0
            while i < n:
                if p[i] <= x and x<p[i+1]:
                    return a[i]
                i=i+1
    
    return piecewise_polynomial 
get_piecewise_polynomial(1,2)

from math import fabs

# BITTE IMPLEMENTIEREN SIE IHRE FUNKTIONEN
# HIER. ÄNDERN SIE NICHT DEN UNTEREN PROGRAMMTEIL.




####################################################################
"""
Bitte den folgenden Teil des Programms nicht mehr editieren:
Hier werden Ihre Funktionen automatisch getestet.

Der assert Befehl erwartet True als Argument, andernfalls wird die
Ausführung des Programms mit einer Fehlermeldung abgebrochen.
"""
assert heaviside(1) == 1
assert heaviside(-1) == 0
assert heaviside(0) == 1
print("a) OK")

assert smoothed_heaviside(-1) == 0
assert smoothed_heaviside(1) == 1
assert smoothed_heaviside(-1e-4) > 0
assert smoothed_heaviside(-1, 2) > 0
assert fabs(smoothed_heaviside(1, 2) - (0.5 + 0.25 + 1/2/math.pi)) < 1e-10
print("b) OK")

a = [1, 2, 3]
p = [-1, 1, 2, 2.5]
polynomial = get_piecewise_polynomial(p, a)
assert polynomial(-10) == 0
assert polynomial(10) == 0
assert polynomial(-1) == 1
assert polynomial(0) == 1
assert polynomial(1) == 2
assert polynomial(2.25) == 3
print("c) OK")

print("Es scheint alles korrekt zu sein! Sehr gut!")

