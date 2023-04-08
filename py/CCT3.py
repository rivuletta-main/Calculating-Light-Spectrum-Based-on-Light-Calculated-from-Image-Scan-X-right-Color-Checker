# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:54:28 2022

@author: rhaen
"""

from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import warnings
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


df = pd.read_csv("Blue.csv")
print(df.head(9))
X = df[['r_org', 'g_org', 'b_org', 'r_cct', 'g_cct', 'b_cct']]
y = df['CCT']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(X,y,test_size=0.1)

from sklearn.ensemble import RandomForestRegressor
dec=RandomForestRegressor()
dec.fit(x_train,y_train)

tahmin = dec.predict(x_test)

y_head = dec.predict(x_test)
from sklearn.metrics import r2_score

yp = dec.predict(X)
r2 = r2_score(y,yp)
print("r2 score: " ,r2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)

model = MLPRegressor(hidden_layer_sizes=(10,5),random_state=1, max_iter=500).fit(X_train, y_train)

model.fit(X_train, y_train)





