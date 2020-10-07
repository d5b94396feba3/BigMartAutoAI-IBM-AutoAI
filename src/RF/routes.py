from flask import render_template, session, request, redirect, url_for, flash, current_app
from src import app
from .predict import predict
from src.Email.email import send_contact_form


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/sample/data/prediction',methods=['POST'])
def sample_predict():

    try:
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3')
        q4 = request.form.get('q4')
        q5 = request.form.get('q5')
        q6 = request.form.get('q6')
        q7 = request.form.get('q7')
        q8 = request.form.get('q8')
        q9 = request.form.get('q9')
        q10 = request.form.get('q10')
        q11 = request.form.get('q11')
        q12 = request.form.get('q12')
        q13 = request.form.get('q13')
        q14 = request.form.get('q14')
        q15 = request.form.get('q15')
        q16 = request.form.get('q16')
        q17 = request.form.get('q17')
        q18 = request.form.get('q18')
        q19 = request.form.get('q19')
        q20 = request.form.get('q20')
        result=predict(q1, q2, q3, q4, q5, q6, q7, q8, q9,
                q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20)

        return render_template('predict.html',res=result)

    except:
        print('Failed')


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


@app.route('/ambition', methods=['GET'])
def ambition():
    return render_template('ambition.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
