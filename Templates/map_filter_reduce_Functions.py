# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:41:28 2018

@author: Sillas
"""




# COM O METODO dir ( dicionario()) exibie todas as funçao q
#podem ser implementadas em dicionario()






import math

#%% Map function 
#
#calculando area para diferentes circulos:
import math

def area(r):
    return math.pi*(r**2)


randii =[1,5,7.1,0.3,10]

# METODO 1: Direct method :

lista = []

for r in randii:
    a = area(r)
    lista.append(a)
    

# Metodo 2 : map function
    
# recebe em priemiro argumento a funçao area
    # em segundo os dados que queremos 
a=map(area,randii) # retorno é um mapa 
list(a)


#%% maps & tuplas

temps = [("berlin",29),("cairo",36),("beunos aires" , 19), ("losangele",26)]

# convertendo a tupla de celcius para fairenheint
c_to_f = lambda data: (data[0],(9/5)*data[1] +32)

# list é usado para mudar o tipo de dado 
list(map(c_to_f,temps))


#%% FULTER FUNCTION É USADO PARA selecionar certos pedaços de dados 
# de uma lista tupla ou etc


# Example : 
# fill all the data above the avarege:

import statistics

data = [1.3, 2.7, 0.8, 4.1,-0.1]
avg = statistics.mean(data)

# vamos agora usar um filtro para verificar os objetos 
#maiores que a media

list(filter(lambda x: x >avg ,data)) # exibe todos valores acima da media


# remove missing data :

countries = ["", "Argentina", "", "brazil", "chile", "" , "colombia ",""]

list(filter(None,countries))


#%% Reduce functiron 

# Warning: so devemos usar essa funçao quando 
# realmente for necessario !!!

from functools import reduce 
data =[2,3,4,5,6,7,8]

multiplier = lambda x,y : x*y

reduce( multiplier , data)

# fazendo a mesma coisa , porem com for loop:

prod = 1
for x in data:
    prod = prod*x

# for é mais intuitivo 

















