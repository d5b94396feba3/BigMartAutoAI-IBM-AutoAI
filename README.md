# BigMartAutoAI
### AutoAI based machine learning application for predicting bigmart sales using python and flask framework.

#### Read medium blog post of this tutorial [HERE!](https://medium.com/@sha-rah646/how-to-create-and-deploy-machine-learning-model-with-watson-studio-autoai-ca1c772124c6) 

#### Step by step tutorials for creating and deploying machine learning model with IBM’s AutoAI [HERE!](https://github.com/d5b94396feba3/bigmart-sales-prediction-with-ibm-cloud-autoai)


<hr>

### Demo 

YouTube : https://youtu.be/o1vSL-k2fcE

<img src="src/static/demos/autoAI_web_app.gif"/>


## Usage

1. Requirements

    * <strong>Python</strong> (version 3.0 or above)

2. Installation
```
    pip install -r requirements.txt
```

3. Setup
     
```
    *** Get IBM Cloud API key and paste in API_KEY:
    
    API_KEY = "<your API key here>"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
```

``` 
    *** Get model deployment ID and replace it with "Your Deployment ID Here" in response_scoring:
    
    payload_scoring = {"input_data": [{"fields": ['Item_Identifier','Item_Weight','Item_Fat_Content',
    'Item_Visibility','Item_Type','Item_MRP','Outlet_Identifier','Outlet_Establishment_Year',
    'Outlet_Size','Outlet_Location_Type','Outlet_Type'], "values": [[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]] }]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/Your Deployment ID Here/predictions?version=2021-04-29', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    
```

```
  *** Mail Configuration (Optional): 
  
      MAIL_SERVER=''   # mail server 
      MAIL_USERNAME='' # mail server username
      MAIL_PASSWORD='' # mail server password
      MAIL_PORT=465
      MAIL_USE_SSL=True
      MAIL_USE_TLS=False    
```


4. Running
```
     python run.py
```
<hr>


### Useful Resources

<ul>
   <li> 
   Sample Project : <a href="https://github.com/IBM/predict-insurance-charges-with-autoai" target="_blank">https://github.com/IBM/predict-insurance-charges-with-autoai</a>
   </li>
<li>
Watson Studio AutoAI : <a href="https://www.ibm.com/cloud/watson-studio/autoai?cm_sp=freelancer-_-AutoAI-_-cta" target="_blank">https://www.ibm.com/cloud/watson-studio/autoai</a>
</li>
<li>
Step by step tutorials : <a href="https://www.ibm.com/cloud/garage/dte/tutorial/ibm-watson-studio-autoai-modeling-rest-us?cm_sp=freelancer-_-AutoAI-_-cta" target="_blank"> https://www.ibm.com/cloud/garage/dte/tutorial/ibm-watson-studio-autoai-modeling-rest-us</a>	
</li>	
<li>Video tutorials : <a href="https://www.youtube.com/watch?v=knxbJgPmD5E" target="_blank">https://www.youtube.com/watch?v=knxbJgPmD5E</a>
</li>
<li>Documentations : <a href="https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html?cm_sp=freelancer-_-AutoAI-_-cta" target="_blank">https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html</a>
</li>
</ul>
 
