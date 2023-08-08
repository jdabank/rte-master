from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
import secrets
import string
import os

load_dotenv()

db_url = os.getenv("DATABASE_URI")
print(db_url)

def generate_secret_key(length=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

secret_key = generate_secret_key()


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
jwt = JWTManager(app)
db = SQLAlchemy(app)

from app import routes, models

print(secret_key)
