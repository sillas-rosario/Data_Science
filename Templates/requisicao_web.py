# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:28:49 2018

@author: Sillas
"""

#%%

import  requests


response = requests.get('http://www.reddit.com/r/programming/') # se a resposta for 200 
# a pagina é valida
print(response)

arq = response.txt