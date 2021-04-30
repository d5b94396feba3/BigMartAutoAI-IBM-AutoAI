
from flask import Flask
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'khgfd45678jhfgg56678dfghjjhg457gffdghf64vhgd3463fghv4'

app.config.from_pyfile('config.cfg')

mail = Mail(app)

urlSTS = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def create_app():
	return app


from src.autoai import routes
from src.Email import email


