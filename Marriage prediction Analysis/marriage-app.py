# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:08:51 2021

@author: sharm
"""

from flask import Flask,request


app=Flask(__name__)

app.config["DEBUG"] = True
import pickle
pickle_in=open('modelfile.pkl','rb')
model = pickle.load(pickle_in)

@app.route('/',methods=["GET"])
def default():
    return '<h1> Rest API  is working</h1>'

@app.route('/predict',methods=['GET'])
def predict():
    
    predicted_age_of_marriage = model.predict([[int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['profession']),
                            int(request.args['country']),
                            int(request.args['height_cm']),
                            int(request.args['gender_male'])
                           ]])
    return str(round(predicted_age_of_marriage[0],2))

    
  

if(__name__)=='__main__':
    app.run(debug=True)
   