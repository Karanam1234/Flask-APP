from flask import Flask,render_template,request
import numpy as np
import pickle

app=Flask(__name__)

@app.route('/')

def start():
    return render_template('result.html')

   #  prediction value
def between(predict):
    data=np.array(predict).reshape(1,12)
    load_model=pickle.load(open('activity_income.pkl','rb'))
    result=load_model.predict(data)
    return result[0]

@app.route('/result',method=['POST'])

def result():
   if request.method=='POST':
      predict=request.form.to_dict()
      predict=list(predict.values())
      predict=list(map(int,predict))
      result=(predict)
    if int(result)==1:
        prediction='income is >50k '
    else:
        prediction='income is <=50k '
    return render_template('result.html')
   if __name__=="__main__":
     app.run(debug=True)
     app.config['TEMPLATES_AUTO_RELOD'==True]
