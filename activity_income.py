# -*- coding: utf-8 -*-
"""activity_income

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19H78wEZBPndc5WRZvTzxkc0xmkzWbFZK
"""

import pandas as pd
import numpy as np
import os

df=pd.read_excel('/content/adult_train.csv',na_values='?')

df.head()

df.shape

df.isnull().sum()

df.dtypes

df.dropna(axis=0,inplace=True)

df.isnull().sum()

df.shape

df.corr()

df.drop('fnlwgt',axis=1,inplace=True)

df.head()

df['workclass'].unique()

df['education'].unique()

df['marital-status'].unique()

df['native-country'].unique()

df['income'].unique()

for col in ['workclass','education','marital-status','occupation','relationship','race','gender']:
  df[col]=df[col].astype("category")

df.dtypes

df['income']=df['income'].astype("category")

df.dtypes

cat_Attr_Names = ['workclass','education','marital-status','occupation','relationship','race','gender']
num_Attr_Names = ['age','educational-num','capital-gain','capital-loss','hours-per-week']

cat_Attr_Names

df[cat_Attr_Names] = df[cat_Attr_Names].apply(lambda col: col.astype('category'))
df[num_Attr_Names] = df[num_Attr_Names].apply(lambda col: col.astype('int64'))

df.head()

df['income']=df['income'].map({'<=50K':0,'>50K':1})

df['income'].value_counts()

df.head()

y=df['income']

x=df.drop('income',axis=1)

y.head()

x.head()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1122,test_size=0.3)

y_train.count()

y_test.count()

y_train.value_counts()

y_test.value_counts()

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from joblib import dump

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, num_Attr_Names),
        ('cat', categorical_transformer, cat_Attr_Names)])

from sklearn import tree

classifier= tree.DecisionTreeClassifier()

clf = Pipeline(steps=[
    ('preprocessor', preprocessor), 
    ('classifier', classifier)])
clf.fit(x_train, y_train
        )

y_pred_train = clf.predict(x_train)

y_pred_train

y_pred_test = clf.predict(x_test)

y_pred_test

from sklearn.metrics import accuracy_score,recall_score

print("Accuracy = ", accuracy_score(y_train, y_pred_train))
print("Recall   = ", recall_score(y_train, y_pred_train))

print("Accuracy = ", accuracy_score(y_test, y_pred_test))
print("Recall   = ", recall_score(y_test, y_pred_test))

import pickle

PATH = os.getcwd()

dump_file = PATH + 'model_01.pkl'

dump(clf, dump_file, compress=1)