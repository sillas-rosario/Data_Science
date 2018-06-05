# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:38:28 2018

@author: Sillas
"""

# Joints with python !!

import pandas as pd

t1 =pd.read_csv("table1.csv")

t2=pd.read_csv("table2.csv")



 # on  allows us to specify which column to join on 
m = pd.merge(t1,t2,on = "user_id")

# metodo alternativo para usar o merge()
#t1.merge(t2, on="user_id")