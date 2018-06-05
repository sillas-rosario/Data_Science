# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:57:58 2018

@author: Sillas
"""

##### Estruturas de laço ###

#%%

nome = [ 'Sillas' , 'julia' , 'tana', '@###' ]
   
        
# python contabiliza quantos itens tem dentro da coleçao 
# e ja imprime        
for n in nome:
    print(n)


# outra maneira de usar o for é com range
    
i = range(5)
print(i)   # range(1,5)


for item in range(4):                    ## item recebe as posiçoes do range
    print(str(item)+ '  ' + nome[item])


for i in range(len(nome)):
    print(nome[i])
    
    
#%%
    
palavra = 'Aprendendo Python'
    
for letra in palavra:
    print(letra)            # cada index refere a uma letra
    
#%%#  while
    
    
i = 1
A = True
while A:
        
    i = i + 1
    if i==5:
        A = False
        break
        

        
print ('acabou while i =', i)    

    
    