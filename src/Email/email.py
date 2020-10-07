
from flask import render_template, request, redirect, url_for, flash, session
from flask_mail import Message
import secrets
from src import app, mail, urlSTS


def recipient_email():
    # return current_user.email
    return 'shahiburrahman55@gmail.com'


def default_email():
    return 'swap.mail.demo@gmail.com'  # mail username


def send_contact_form(name,email,message):

    recipient = recipient_email()
    sender = default_email()
    msg = Message('New Contact Form From ThyroidML', sender=sender, recipients=[recipient])
    msg.html = render_template(
        'email/contact_form.html',name=name,email=email,message=message)
    mail.send(msg)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
