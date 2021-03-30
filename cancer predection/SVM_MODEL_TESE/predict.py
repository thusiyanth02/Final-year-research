import os 
import json
import pandas as pd
import numpy
from sklearn.externals import joblib

s = pd.read_json('./input.json')
p = joblib.load("./SVM_model.pkl")
r = p.predict(s)

print (str(r))

