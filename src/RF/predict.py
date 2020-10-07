from .build import random_forest,X_test,y_test,metrics
from flask import render_template, session, request, redirect, url_for, flash, current_app
from .model import DatasetThyroid
from src import app,db

def predict(q1, q2, q3, q4, q5, q6, q7, q8, q9,
            q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20):

    res_dict={}
    result = random_forest.predict([[q1, q2, q3, q4, q5, q6, q7, q8, q9,
                                q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]])
    y_pred = random_forest.predict(X_test)
    pred = random_forest.predict_proba([[q1, q2, q3, q4, q5, q6, q7, q8, q9,
                                        q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]])

    res_dict['result']= result

    res_dict['overall_accuracy'] = "{0: .2f} %".format(
        metrics.accuracy_score(y_test, y_pred)*100)

    res_dict['ratio']=pred[0]
    if result == 0:
        result = 0

    else:
        result = 1

    try:
        dataset = DatasetThyroid(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9,
                                q10=q10, q11=q11, q12=q12, q13=q13, q14=q14, q15=q15, q16=q16, q17=q17, q18=q18, q19=q19, q20=q20, res=result)
        
        db.session.add(dataset)
        db.session.commit()
    except Exception as e:
        print('failed to insert', e)

    return res_dict



