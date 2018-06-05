# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:40:21 2018

@author: Sillas

 Comparando modulos desenvolvidos com e sem a biblioteca NUMPY
"""

import numpy as np


L =[1,2,3]

A=np.array([1,2,3])

for e in L:
    print (e)


for e in A:
    print(e)

## Os dois realizam a mesma funçao

L.append(4)
print(L)
L = L +[5]
print(L)
#  No numnpy object nao é possivel utilziar o append()
#A.append(4)

#%%

 #% Primeira diferença , para realizar operaçoes matematias
 #% com o a lista é rpeciso usar for que é muito lento 
 #% ja com o nympy essas operaçoes podem ser feita diretamente , 
 # Observe abaixo :  
 
A = np.array([2,3, 4])

print (A)

print("A+A  = "  , A+A)

print("2*A = ", 2*A )  # multiplica 2 por todos elementos do veotr

print( "A**2 = " , A**2) # eleva todos elemento ao quadrado
 
print("sqrt(A) = " , np.sqrt(A))  #tira raiz de todos elementos













