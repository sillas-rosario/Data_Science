# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:29:45 2018

@author: Sillas
"""

 # dit product > for loop vs . cosine methoed vc , dot function
 
import numpy as np 
 
 
a = np.array([1,2])
 
b = np.array([2,1])
 
dot = 0
 
# funçao zip :
# [ 1, 2, 3 ]
#  zip--------------- ====> [(1, 4), (2, 5), (3, 6)]
#  [ 4, 5, 6 ]
 
 
for e ,f in zip(a,b):
     dot += e*f


#% bruncando com  zip
l=[];
for e,f in zip(a,b):
    l.append([e , f])

#%% multiplicaçao arrays together

a = np.array([1,2])
 
b = np.array([2,1])

print(a*b)

  #% u can't do it with arrays that are difente size:
  
print(np.sum(a*b))

print((a*b).sum())

print(np.dot(a,b))

print((a).dot(b))


# exemplo usando o dot()
 # para multiplicar matrize s AX = B
 
A=np.eye(2)
B= np.ones((2,2))*2
A.dot(B)
# resposta é multiplicaçao de matrizes

#%%  Para fazer uma conta cumum que de um metod e de analise
#$ de datas

a = np.array([1,2])
 
b = np.array([2,1])



amog = np.sqrt( (a*a).sum())
print(amog)
# restorna o mesmo resutlado de :
amog =np.linalg.norm(a)
print(amog)

cosangle = a.dot(b) / (np.linalg.norm(a)* np.linalg.norm(b))
print(cosangle)











