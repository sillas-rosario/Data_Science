# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:35:41 2018

@author: Sillas
"""

#%% Aplciaçao com lambda : 

# lambda é muuito usuavel quanto temos que fazer uma funçao rapida



strin = '0000000this is string example....wow!!!0000000';
strin = strin.strip( '0' ).title() # retorna a str sem zeros ||
# e o title , poe as palavras em maiusculo 


full_name = lambda fn,ln: fn.strip('l').title()+ " " +ln.strip().title()

full_name('sillas',"rosario")

#
#ANOTHER EXEMPLO:

scifi_authores = [ "Isaac Asimov","ray bradbury", "robert Heilein", "Arthur Clarke", "Orson Scott Card",
                  "H. G. Wel"]

#% index [-1] informa que o split sera realziado no ultimo valor 
# lower() é para evitar a sensibulidade com letras maiusculas

scifi_authores.sort(key = lambda name: name.split(" ")[-1].lower())





## ANother exemplo :

def build_quadratic_function(a,b,c):
     return lambda x: a*x**2 + b*x + c
 

f = build_quadratic_function(2,-3,5)



build_quadratic_function(3,0,1)(2) # 3x^2 + 1 evaluated for x=2







