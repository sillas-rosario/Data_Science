# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:21:06 2018

@author: Sillas
"""

import numpy as np


# matriz usando numpy
M = np.array([[1,2],[3,4]])

# matriz usando lista
L = [[1,2],[3,4]]

# acessando both:

print("L[0] = " , L[0])

print("L[0][0] = ", L[0][0])

print("M[0,0] = ", M[0,0])


## difereça entre np.array e np.matrix

M2 = np.matrix([[1,2],[3,4]])

## é semrpe melhor usar um array , se vermos uma matrix é sempre melhor 
# converter para array 

M3 = np.array(M2) 



#%%   COMO CRIAR ARRAYS :

Z=np.zeros(10)

Z1=np.ones((10,10))

R = np.random.random((10,10))

R1 = np.random.randn(10,10)

R1.mean()
R1.var()

#%%  Matrix products

# pre requisitos para mutiplicar matrizes 
# 

A = np.matrix([[1,2] , [1,2]])
B = np.matrix([[2,1], [2,1]])


print( A*B )
print( A.dot(B) )

 
#%%  

A = np.array([[1,2] ,[3,4]])

print(" matrix A :" , A)

ainversa = np.linalg.inv(A)

print("Inversa de A : ", ainversa)

# para confirmar , se mutiplicar A*inv(A) = I

print(" confirmando A*inv(A) = ", A.dot(ainversa) )

determinante = np.linalg.det(A)

diagonal = np.diag(A)

print("determinandte : " , determinante , " matrix diagonal : " , diagonal) 

a = np.array([1,2])
b = np.array([3,4])

d=np.inner(a,b) #  = sum(a[:] * b[:])

o = np.outer(a,b) # produto entre linhas e colunas

c = np.diag(A).sum() # soma das diagonais 

e = np.trace(A) # mesma coisa

# eig-values e eig-vectors

X=np.random.randn(100,3)

# existe  dois tipos de achar o auto valor e auto vetor
X = no.cov(X.T)
eig_vectors = np.linalg.eig(X)

#%%  SOLVING A LINEAR SYSTEM

A = np.array([[1,2] ,[3,4]])
b = np.array([1,2])
x = np.linalg.inv(A).dot(b)

print( "LINEAR SOLUTION ", x)

# ACIMA FOI REPRESENTADO UMA MANEIRA , POREM O MELHOR 
#METODO PARA REALIZAR ISSO É COM O .SOLVE()

x = np.linalg.solve(A,b)
print(x)



#%% linear problem



c = np.array([[1 , 1],[1.5 , 4]])

b = np.array([2200, 5050])

c = np.linalg.solve(A,b)





















