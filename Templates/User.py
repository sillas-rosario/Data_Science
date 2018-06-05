# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:26:01 2018

@author: Sillas
"""

class User():
    """
    Adicionar o texto para servir de lembrete sobre as funçoes 
    implementadas na funçao abaixo qunado usando help(User)
    
    """
    def__init__(self, full_name, birthday)
        self.name = full_name
        self.birthday = birthday
        
        #extract firs and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name  = name_pieces[-1] 