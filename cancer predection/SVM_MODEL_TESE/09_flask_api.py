import os 
import json
import pandas as pd
import numpy
from flask import Flask, render_template, request, jsonify
from pandas.io.json import json_normalize
from sklearn.externals import joblib

app = Flask(__name__)
port = int(os.getenv('PORT', 8080))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/model', methods=['POST'])
def model():
    if request.method == 'POST':
        try:
            post_data = request.get_json()
            json_data = json.dumps(post_data)
            s = pd.read_json(json_data)          
            p = joblib.load("./SVM_model.pkl")
            r = p.predict(s)
            return r
        
        except Exception as e:
            return (e)
			
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=True)
