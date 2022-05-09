import flask; print(flask.__version__)
from flask import Flask, render_template, request
import os
import numpy as np
import pickle

app = Flask(__name__)
result = ""

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Request.method:", request.method)
    print("Request.TYPE", type(request))
    if request.method == 'POST':
        print(request.form)
        age = request.form['age']
        sex = request.form['sex']
        job = request.form['job']
        housing = request.form['housing']
        saving_account = request.form['saving_account']
        checking_amount = request.form['checking_amount']
        credit_amount = request.form['credit_amount']
        duration = request.form['duration']
        purpose = request.form['purpose']

        test_arr = np.array([age, sex, job, housing, saving_account, checking_amount, credit_amount, duration, purpose])
        model = pickle.load(open('ml_model.pkl', 'rb'))
        print("Model Object: ", model)
        prediction = model.predict(test_arr)
        predicted = "Risky" if prediction else "No Risk" 
        result = f"The model has predicted that the result is: {predicted}"
        return render_template('index.html', result=result)
    return render_template('index.html')

app.run(host='0.0.0.0', port=81, debug=False)