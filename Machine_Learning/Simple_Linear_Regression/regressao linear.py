# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 23:31:50 2018

@author: Sillas
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

#splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split   
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 1/3, random_state = 0)

# features scaling

'''from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train=sc_X.fit_transform( X_train)
X_test=sc_X.transform(X_test)'''


#fitting linear regreation

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting vector
y_pred = regressor.predict(X_test)

#visualizing the prediction of training set
plt.scatter(X_train,y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience')
plt.show()
# visualizing the preditcion of test set results
plt.scatter(X_test,y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience')
plt.show()
