import os 
import random
import json
import pandas as pd
import numpy
from flask import Flask, render_template, request, jsonify
from pandas.io.json import json_normalize
from sklearn.externals import joblib
from werkzeug.wrappers import Request, Response


app = Flask(__name__)
port = int(os.getenv('PORT', 5500))

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/api/model', methods=['POST'])
def model():

for x in range(10):
  y= random.randint(1,21)
   
     return (y)
	
        
        except Exception as e:
            return (e)
			
if __name__ == '__main__':

	app.run(host='0.0.0.0', port=port, debug=True)
