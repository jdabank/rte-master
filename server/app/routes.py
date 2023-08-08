from app import app
from flask import request, jsonify
from flask_jwt_extended import create_access_token

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
