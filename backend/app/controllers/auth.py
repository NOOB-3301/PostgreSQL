from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db
from . import api_bp


@api_bp.route('/auth/register', methods=['POST'])
def register():
    print('register hit')
    data = request.json
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@api_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

# @api_bp.route('/test', methods=['GET'])
# def test():
#     return jsonify({'message': 'Test successful'}), 200