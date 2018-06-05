# -*- coding: utf-8 -*-
"""
Created on Thu May 31 08:30:20 2018

@author: Sillas

this code I am gonna approch CSVs in python 
by Udacity

there are two ways to represent a CSV file :
    Option 01 : Each row is a list
    Option 02 > Each row is a dictionary



"""
import unicodecsv

#%%
# creating list of enrollments
enrollments = []

# rb  =  file will be open for reading and b change the format 
f  = open('enrollments.csv', 'rb')

# DicReader means that each row will be a dictionary 
# It have been chosed since our data does have a Header row
# What allow me to refer to each colum by its name
# rether than its number
reader = unicodecsv.DictReader(f)


# the interater only allow to loop over 
# the data once 
for row in reader:
    enrollments.append(row)

# closing the file 
f.close()


#%%  Handcut statement 

with open('enrollments.csv', 'rb') as f:
    reader  = unicodecsv.DictReadar(f)
    
    # I can created the list without go over the loop
    enrollments = list(reader)
      
    
#%%  reading two others CSV file 
    
    
def read_csv( filename ):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        f = list(reader)
        return f[0]
    
    


print(read_csv('daily_engagement.csv'))       
print(read_csv('enrollments.csv'))  

#%% FIXING  CSV DATA


from datetime import datetime as dt
 
def parse_date (date):
    """  info :  if there is no data in returns None 
           otherwise it return data in a proper format  """
    if date == '':
        return None
    else: 
        return dt.strptime(date,'%Y-%m-%d')

def parse_maybe_int(i):
    if i == '' :
        return None
    else: 
        return int(i)
 
with open('enrollments.csv', 'rb') as f:
    reader  = unicodecsv.DictReader(f)
    
    # I can created the list without go over the loop
    enrollments = list(reader) 
 
 # clean up the data types in the enrollments table 
for enrollments in enrollments:
     enrollments['cancel_date'] = parse_date (enrollments['cancel_date'])
     enrollments['days_to_cancel'] = parse_maybe_int(enrollments['days_to_cancel'])
     enrollments['is_cancelled'] = enrollments['is_canceled'] == 'True'
     enrollments['is_udacity'] = enrollments['is_udacity'] == 'True'
     enrollments['join_date'] = parse_date (enrollments['join_date'])
     










    
    
