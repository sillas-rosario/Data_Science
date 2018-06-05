# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:22:01 2018

@author: Sillas
"""

## Lista duplas tuplas dicionario :
#%%  lISTA [] É MUTAVEL
lista = [ 1, 2, 3, 4, 5]
print('isso é uma lista  : ' , lista[1:len(lista)])


#%%   TUPLAA ()  NAO É MUTAVEL , NAO EXISTE APPEND EXTEND ETC....

trab_tuplas =( 1, 2, 3 ,4 , 5)

# é usuavel quando tivermos um numero limitados de coisas !! 
# ela é estatica !!


#%% Dicionario { }  semrpe tem uma chave e um valor 
# como em um dicionario memso , ele tem uma chave_palavra e o valor
               
        # dicts #keys  : value #  
 tab_dic = {  'valor': 10,
              'nome' : 'Sillas',
              'idade': 25
              }
 
 print(tab_dic)

a = tab_dic.get('valor')
print(a)  # valor = 10



b = tab_dic.keys()
print(b)
# o dicionario nao permite  escrever mais de um tipo , por exemplo , 
# se escrever idade mais uma vez , o dicionario sobrescreve a anterior
#%%
dic_p2 = {}
dic_p2['primeira'] = 1
dic_p2['segunda'] =2

#print (dic_p2) # exibe o dicionario criado

#print( dic_p2.keys())

for key in dic_p2.keys():
    print(" chave :", key ," , valor :", dic_p2[key])

k = list(dic_p2.keys())
print (k)


## testando se chave esta no direitorio usando o (((((( in e not in ))))))

inventory = {'pears': 430, 'bananas': 312, 'oranges': 525, ' apples': 217}
print('apples'  in inventory)  # retorno é true
print('cherries' in inventory) # retorna falso

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

#%%
inventory = {'pears': 430, 'bananas': 312, 'oranges': 525, ' apples': 217}
invent_sort = list(inventory.keys())
print(invent_sort.sort())


#%% 

mydict = { 'hi':'oi', 'how to': 'como' , 'in': 'em' , 'python': 'python', '?': '?', 'code': 'programar' }

v = " como programar em python"

 analise = list(v)
 
       
    





















