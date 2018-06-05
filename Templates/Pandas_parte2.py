# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:06:58 2018

@author: Sillas
"""

import pandas as pd

# skipfoot =3 ( skip the tre frist rows)
# skipfoot does not work without engine documentetion thats qhy we add it out
df = pd.read_csv('international-airline-passengers.csv',engine="python",skipfooter = 3)

# resigning the columns
df.columns = ['month' , 'passangers']

# podemos acessar 
print(df['passangers'])


# cria uma nova coluna e acrescenta 1 
df['ones'] = 1

print(df.head())







#%% THE APPLY() FUNCTION:


from datetime import datetime

datetime.strptime("1949-05","%Y-%m")

# What do we do if we want assing a new column with difetens values:

# criar uma nova coluna com valores referentes as colunas exitentes
# nao usar for pois sao muito lentos ; jeito de fazer isso é com a 
# funçao apply()

df['x1x2'] =df.apply(lambda row: datetime.strptime(row['month'],"%Y-%m"), axis =1)

# axis =1 funçao gets applied across each row insteado of each colum










