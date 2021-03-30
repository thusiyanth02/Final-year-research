import os 
import json
import pandas as pd
import numpy
from sklearn.externals import joblib

s = pd.read_json('./input.json')
p = joblib.load("./classifier_model.pkl")
r = p.predict(s)

if r==0:
  print("Not Cancer")

print ("cancer")
print(r)
 

