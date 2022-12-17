import pickle
from flask import Flask,redirect,request,render_template,app,jsonify,url_for
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
import joblib

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('result.html')

@app.route('/result',methods=['POST'])
def predict():
    data=[request.form.values()]
    print(data)
    load_model=pickle.load(open('activity_income.pkl','rb'))
    output=load_model.predict(data)[0]
    return render_template('result.html',submit='Employee salary is{}'.format(output))
"""def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    output=model.predict(data)
    print(output[0])
    return jsonify(output[0])"""

if __name__=='__main__':
    app.run(debug=True)
    


