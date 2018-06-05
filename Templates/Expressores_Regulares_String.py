# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:07:27 2018

@author: Sillas
"""

# Expressoes Regulares

# .   qualquer caracter exceto o de quebra linha 
# ^   a partir do inicio da linha 
# $   correspondencia ate o final da linha 
# []  indica um conjunto de caracteres
# *   ha correnspondencia com nenhum ou mais 
# +   ha correnspondencia com um ou mais de um 
# |   A|b  corresponde a um ou outros sendo que estes apresentam mesmo conjunto


import re

#%% Recuperar todos os numeros de ponto flutuante da string

string = " 5.0 +4.0 "
pattern =  "(5.0)|(4.0)"

print(re.findall(pattern,string))


# A ideia do pattern  é utilizar como padrao, para que durante 
# a recuperaçao dos ponto flutuante o findall possa avaliar e dar encontrar
# o ponto flutuante de acordo com o conjunto de caracteres[] que foi passado abaixo
# imprementaçao é feita seguindo a seguinte ideia:
#  numero.pontoflutuante =  5.0 (exemplo)
# por isso passamo [0-9] para valores antes e dp do ponto 
# a barra é colocada pq por default ele consideraria como qualuer digito
pattern =  "[0-9]\.[0-9]"
print(re.findall(pattern,string))

#%%
# para o caso em que queremos analisar uma string do tipo 
string = "5555.000555 +2.0"
 
pattern = "[0-9]+\.[0-9]+"
# '*' = enquanto tiver um caracter antes do digito que nao seja ponto 
# ele deve dar match 
print(re.findall(pattern,string))

#%% 

# Outra forma de representar os digitos 
# \d => equivalente => [0-9]


#%%
 nome =""" Sillas Rosario Costa Engenharia  Mecatronica. """
 
 #padrao = Letras MaiusculasMinusculas(\s é para espaço) 
pattern = "([A-Z][a-z]+\s)"

print(re.findall(pattern,nome))

# note que a resposta nao apresenta Mecatronica 
# pois mecatronica possui o ponto '.' no final 
# ou seja nao deu match com o pattern 

# soluçao para casos ontem temos um espaço ou mais de um espaço 
 pattern = "([A-Z][a-z]+\s*)+"
 print(re.findall(pattern,nome))