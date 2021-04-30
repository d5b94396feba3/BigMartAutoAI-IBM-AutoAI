from src import app
from src.Email.email import send_contact_form

from flask import Flask, url_for, render_template, redirect
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Response
import urllib3
import json

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/sample/data/prediction',methods=['POST'])
def sample_predict():

    req = request.form
    q3 = req.get('Item_Fat_Content')
    q1 = req.get('Item_Identifier')
    q6 = float(req.get('Item_MRP'))
    q5 = req.get('Item_Type')
    q4 = float(req.get('Item_Visibility'))
    q2 = float(req.get('Item_Weight'))
    q8 = int(req.get('Outlet_Establishment_Year'))
    q7 = req.get('Outlet_Identifier')
    q10 = req.get('Outlet_Location_Type')
    q9 = req.get('Outlet_Size')
    q11 = req.get('Outlet_Type')


    API_KEY = "<your API key here>"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": ['Item_Identifier','Item_Weight','Item_Fat_Content',

    'Item_Visibility','Item_Type','Item_MRP','Outlet_Identifier','Outlet_Establishment_Year',
    'Outlet_Size','Outlet_Location_Type','Outlet_Type'], "values": [[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]] }]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/"Your Deployment ID Here"/predictions?version=2021-04-29', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response: ")
    print(response_scoring.json())
    
    res = json.loads(response_scoring.text)

    for key in res:
      ab = res[key]
    

    for key in ab[0]:
      bc = ab[0][key]
    
    res = round(bc[0][0])
    print('Predicted Outlet Sales:',res)

    return render_template('predict.html',res=res)




@app.route('/quick/test',methods=['GET','POST'])
def quick_test():
    return render_template('quick_test.html')


@app.route('/faq', methods=['GET'])
def faq():
    return render_template('faq.html')


@app.route('/contact', methods=['GET','POST'])
def contact_us():
    if request.method=="POST":
        name= request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        send_contact_form(name,email, message)
        return render_template('thank.html')

    return render_template('contact.html')


@app.route('/resources', methods=['GET'])
def resources():
    return render_template('resources.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
