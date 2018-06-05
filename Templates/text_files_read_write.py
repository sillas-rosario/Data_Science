# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:39:56 2018

@author: Sillas
"""

# how to WRITE & READ txt files:

# we are going to approach both good and very good techiniquis 
# to treat this matter

# any doubt acess help (open)

#%%
f = open("guido_bio.txt")
# by defoult it opens the file in read mode and
# return a file object f

text = f.read()
# this will return all the text in the file

f.close()


#%% melhor jeito de fazer isso:

#com essa tecninca nao precisa fechar o file
with open("guido_bio.txt")  as fobj:
    bio= fobj.read()

#print(bio) no console
    
    
#%% tentar abrir um file que nao existe:

try:    
 with open("future_lottery.txt") as f:
      text = f.read()
      
except FileNotFoundError:
    text = None      
    


#%% criando files:

#write
oceans = [ "pacific", "atlantic", "indian"," southen","artic"]

# "w" = write
# "r" = read
# "a" = append
# se nao especificar o modo o python vai abrir em read
# read mode by default
with open("oceans.txt","w") as f:
    # se o ocean.txt nao existe, python vai criar 
    # e se ja existe o python vai dar u overwrite
    for ocean in oceans:     
        f.write(ocean)
        f.write("\n")
        
        
       
    

#%% 
        
        
with open("oceans.txt","a") as f:
  
    print(23*"*=",file=f)
    print("there are the 5 oceans.",file=f)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

