
from flask import render_template, request, redirect, url_for, flash, session
from flask_mail import Message
import secrets
from src import app, mail, urlSTS


def recipient_email():
    return 'Recipient Mail username here'

def default_email():
    return 'Sender Mail username here'  # mail will be sent from this mail username

def send_contact_form(name,email,message):

    recipient = recipient_email()
    sender = default_email()
    msg = Message('New Contact Form From BigMartAutoAI', sender=sender, recipients=[recipient])
    msg.html = render_template(
        'email/contact_form.html',name=name,email=email,message=message)
    mail.send(msg)


