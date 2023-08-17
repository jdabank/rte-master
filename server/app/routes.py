from app import app, db
from models import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

@app.route('/')
def index():
    return "Hello!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if valid:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401
    

@app.route('/register', methods=['POST'])
def register():
   username = request.json.get('username')
   password = request.json.get('password')

# Check if the username already exists in the database
   existing_user = User.query.filter_by(username=username).first()
   if existing_user:
    return jsonify(message='Username already exists'), 400

    # Hash the password before saving it
   hashed_password = generate_password_hash(password, method='sha256')

    # Create a new User instance and add it to the database
   new_user = User(username=username, password=hashed_password)
   db.session.add(new_user)
   db.session.commit()

   return jsonify(message='User registered successfully'), 201