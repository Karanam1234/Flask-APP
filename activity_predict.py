# Import libraries
import os
from joblib import load
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score

PATH = os.getcwd()

clf = load(PATH + '/activity_income.pkl')

data = pd.read_excel(PATH+"/adult_test.csv")

y_pred = clf.predict(data)

data["y_pred"] = y_pred

