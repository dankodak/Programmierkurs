
# coding: utf-8

# In[ ]:


import math 
def Guthaben(b,p,n):
    l = b*(1+p/36000)**n
    return l
def Anfangsbetrag(a,p,n):
    m = a*(1+p/36000)**(-n)
    return m
def Anzahltage(b,a,p):
    o = math.log(a/b)/math.log(1+p/36000)
    return o
def Zinsatz(a,b,n):
    q = 36000((a/b)**(1/n)-1)
    return q

