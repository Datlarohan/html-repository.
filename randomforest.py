import numpy as np
import pickle 
from flask import Flask , render_template , url_for , request

app=flask(__name__)
Model = pickle.load(open('RF_Model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/details')
def PredictstartUp():
    return render_template('predictstartup.html')

@app.route('/Predictstartupfuture', methods=['POST'])
def Predicttartupfuture():

    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = Model.predict(final_features)

    output = prediction[0]
    if output == 1:
       predictionText = 'Failed'
    elif output == 3:
        predictionText = 'Succesful'