# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:44:21 2018

@author: Sillas
"""

#Quiz Questions about Student Data:
#    1 Ho long to submit projects
#    2 how do students who pass
#    3 their projets differs from thow who dont ?
#    
#   THE OTHER QUESTION 
#   How much time students spend taking classes
#   hor time spent relates to lessons / projects completed


import unicodecsv
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
    

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


def number_of_rows(table):
   return len(table)




# first step : reading :
enrollments = read_csv("enrollments.csv")
daily_engagement =  read_csv("daily_engagement.csv")
project_submissions = read_csv("project_submissions.csv")

 # clean up the data types in the enrollments table :
for enrollment in enrollments:
     enrollment['cancel_date'] = parse_date (enrollment['cancel_date'])
     enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
     enrollment['is_cancelled'] = enrollment['is_canceled'] == 'True'
     enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
     enrollment['join_date'] = parse_date (enrollment['join_date'])


# Second Step : Fiding the number of rows in the table:
enrollment_num_rows = number_of_rows(enrollments)
print("\n\nenrollments number of rows {}".format( enrollment_num_rows))


# For each of these three tables, find the number of rows in the table and
# the number of unique students in the table.To find the number of unique
# students, you might want to create a set of the account keys in each table.

# enrollment :

enroll_unique_student = set() # new empty set object
for enroll in enrollments:
    enroll_unique_student.add(enroll['account_key'])    
print ("unique_enrollments = {}".format(len(enroll_unique_student)))


 
# daily_engagement:

unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['acct'])
    
print("daily_ unique = {}".format(len(unique_engagement_students)))

# project submissions:

project_unique = set()
for pro_sub in project_submissions:
    project_unique.add(pro_sub['account_key'])
print("project_submissions = {}".format(len(project_unique)))





#%% Problems in the Data:

# first thing I am going to do is rename the 
# Acct column by putting Account_Key as replace
# once both is about the same thing

for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]
    
    
    

# Investigating missing students from daily_engagement :
 
for enroll in enrollments:
    student  = enroll['account_key']
    if student not in unique_engagement_students:
        print (enrollment)
    
    
    
    






























