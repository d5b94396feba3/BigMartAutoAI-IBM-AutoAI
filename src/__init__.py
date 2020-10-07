
from flask import Flask
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'khgfd45678jhfgg56678dfghjjhg457gffdghf64vhgd3463fghv4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_thyroidML.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

mail = Mail(app)

urlSTS = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def create_app():
	return app


from src.RF import routes
from src.RF import build
from src.Email import email
from src.RF import model


