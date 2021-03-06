# -*- coding: utf-8 -*-
"""Covid 19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QPuOo0HiWPNmCHiglRjVCWYZeHXkjuyx
"""

import numpy as np
import pandas as pd
import seaborn as sb

"""Data Importing"""

url='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
data=pd.read_csv(url,index_col="location")

data.head()

first=data.loc["India"]

"""Data Cleaning"""

first.fillna(0,inplace=True)

first

"""Data Vissualization"""

first.corr()

sb.heatmap(first.corr())

sb.displot(first.corr())

sb.distplot(data['people_fully_vaccinated'])

sb.distplot(first['people_vaccinated'])

"""Array Creation


"""

X=first[['total_vaccinations','people_vaccinated','total_vaccinations_per_hundred','people_vaccinated_per_hundred']]
Y=first[['people_fully_vaccinated']]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=25000)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,Y_train)

lr_pred=lr.predict(X_test)
print(lr_pred)

lr_a=lr.score(X_test,Y_test)
print(lr_a)

