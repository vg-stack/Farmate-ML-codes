# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17fwSWkhM5sDivs_vx9I79QMMkrPW7LvF
"""

from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('croprec.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('service.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['null']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
    pred = model.predict(arr)
    return render_template('after1.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)