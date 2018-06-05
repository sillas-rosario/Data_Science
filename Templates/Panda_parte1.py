# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:48:33 2018

@author: Sillas
"""

# LOADING DATA 
# Unstructured data - the internet 
# semi-structured data - apache logs

# Structured data =Kaggle and other dataset (usually CSV)
# CSV = COMMA SEPARATED VALUES 

# EACH ROW IS A RECORD 
# EACH RECODS'S VALUES ARE SEPARETED BY COMMAS
# ITS A TABLE SO YOU CAN OPEN IN EXCEL



D = []
import numpy as np

# Nao esta funcionando propriamente



# funçao map tranforma a linha da lista em  float 


for line in open("data_2d.csv"):
  row = line.split(',')
  sample = map(float, row)
  D.append(row)
  
D = np.array(D)    


#%%# DATA FRAME PANDAS !!

import pandas as pd

# header = none 
X = pd.read_csv("data_2d.csv",header=None)

print(type(X))

print(X.info())

# essa funçao exibe os primeiros dados 
print(X.head())


# Quando usamos Numpy array X[0]- 0th row
# Quando usamos Pandas X[0] -> Column that has name O
# check it out
print(X[0])

print(type(X[0])) # RTETURN SERIES pois tudo em pandas é series

print( X.iloc[0]) 
# retorna  a linha 0

print(X.ix[0]) 

print( X [ X[0] < 5 ]) # valores retornados na coluna 0 serao menores que 5

# X[0] <5 : retorna um boolean value

















