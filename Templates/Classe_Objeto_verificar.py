# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:07:05 2018

@author: Sillas
"""

# classes e objetos:


class User():

    def __init__ (self, full_name , birthday):
          self.full_name = full_name
          self.birthday = birthday 
          name_pieces = full_name.split(" ")
          self.first_name = name_pieces[0]
          self.last_name  = name_pieces[-1] 
        



user = User("sillas rosario","1112434")

print(user.first_name)
print(user.last_name)
print(user.birthday)



