# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:57:36 2018

@author: Sillas
"""


from math import factorial



n =int(input ("Digite um numero : "))
f=factorial(n)

print ("o fatorial de {} é {}.".format(n,f))

#%%
n =int(input ("Digite um numero : "))

c=1
while c<=n:
    print('{}'.format(c), end='')
    c +=1