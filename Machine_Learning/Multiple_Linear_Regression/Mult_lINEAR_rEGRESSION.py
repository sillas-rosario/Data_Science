# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:05:18 2018

@author: Sillas
"""

import numpy as np
import matplotlib.pyplot
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values


# encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder 

labelencoder_X = LabelEncoder() # criaçao de um objeto do tipo encoder
X[:,3] = labelencoder_X.fit_transform(X[:,3]) 

onehot = OneHotEncoder(categorical_features = [3])
X = onehot.fit_transform(X).toarray()

#dummy variable trap:
X = X [:,1:]





#splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split   
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 0.2, random_state = 0)

# features scaling
#from sklearn.preprocessing import StandardScaler
#sc_X= StandardScaler()
#X_train=sc_X.fit_transform( X_train)
#X_test=sc_X.transform(X_test)

#Fitting Multiple linear Regression

from sklearn.linear_model import LinearRegression

regressor= LinearRegression()
regressor.fit(X_train,y_train)

# prediction
y_pred=regressor.predict(X_test)


import statsmodels.formula.api as sm
# axis =1 add colula , axis=0 add linha ...
# mnudamos a ordem para que a coluna de 1 apareca no inicio
# a funcao abaixo adiciona a coluna de 1 na primeira pocisao afim de representar 
#a constante b0*x0
X=np.append(arr= np.ones((50,1)).astype(int), values=X, axis=1)
# agora todos os modelos foram passados para X-opt
X_opt= X[:,[0, 1, 2, 3, 4, 5]]

regressor_ols= sm.OLS(endog = Y, exog= X_opt).fit()
regressor_ols.summary()

# verificando a resposta do summary() precisamos remover x1 e x2 pois ambos
# possuem p-value elevado, apos essa operacao é preciso vericiar novamente  o p-value

X_opt= X[:,[0, 1, 3, 4, 5]]
regressor_ols= sm.OLS(endog = Y, exog= X_opt).fit()
regressor_ols.summary()

X_opt= X[:,[0, 3, 4, 5]]
regressor_ols= sm.OLS(endog = Y, exog= X_opt).fit()
regressor_ols.summary()

X_opt= X[:,[0, 3, 5]]
regressor_ols= sm.OLS(endog = Y, exog= X_opt).fit()
regressor_ols.summary()

X_opt= X[:,[0, 3,]]
regressor_ols= sm.OLS(endog = Y, exog= X_opt).fit()
regressor_ols.summary()








