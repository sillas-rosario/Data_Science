# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:37:29 2018

@author: Sillas
"""

##### Lista e  string  LISTA COMEÇA EM INDEX 0

#%%
frase = 'oi tudo bem ?' 

lista = [ 'sillas', 'Tana','juju']

print (frase , lista[1])  # print (frase  + lista[1])

print (frase, lista[1 : 3]) # pode colocar o passo na string tb 

print(frase[::-1])  # esta varrendo todos os itens porem ao contrario

#%%
# app end
lista.append('abrava')

print(lista)

lista.remove('sillas')

print(lista)

#%% Insert ( index,'inserindo')

lista = [ 'sillas', 'Tana','juju']
lista.insert( 1 ,'inserindo_iten')

print(lista)

lista[0] = 'inserindo por index'
print(lista)

#%%  funçao count me fala quantas vezes apareceu o joao

lista = [ 'sillas', 'Tana','juju','sillas']

contador = lista.count('sillas')
print(contador)



#%% Funçao len

lista = [ 'sillas', 'Tana','juju','Sillas']
tam =len(lista)
print(tam)

print(lista.pop())  # funçao pop pega o ultimo termo da lista e tambem retira ele da matrix

print(lista)

print(lista.pop(2))  # informa a posiçao 
 print(lista)



