# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:41:18 2018

@author: Sillas
"""

import numpy as np
import matplotlib.pyplot
import pandas as pd

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split   
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 0.2, random_state = 0)

# features scaling

from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train=sc_X.fit_transform( X_train)
X_test=sc_X.transform(X_test)