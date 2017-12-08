
# coding: utf-8

# In[2]:


from math import log
def endbetrag(Ao,n,p):
    A=Ao*(1+p/(360*100))**n
    return A
def anfangsbetrag(A,n,p):
    Ao=A(1+p/36000)**-n
    return Ao
def anzahldertage(A,Ao,p):
    n=log(A/Ao)/(log(1+p/36000))
    return n
def Zinssatz(A,Ao,n):
    p=36000((A/Ao)**(1/n)-1)

