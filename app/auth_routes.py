from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256
from marshmallow import ValidationError
from app import db
from app.models import User
from app.schemas import UserSchema, UserLoginSchema

bp = Blueprint('auth', __name__)
user_schema = UserSchema()
login_schema = UserLoginSchema()

@bp.route('/register', methods=['POST'])
def register():
    try:
        data = user_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    # Check if user already exists
    existing_user = User.query.filter_by(name=data['name']).first()
    if existing_user:
        return jsonify({'error': 'User with this name already exists'}), 400
    
    # Hash password
    hashed_password = pbkdf2_sha256.hash(data['password'])
    
    # Create user
    user = User(
        name=data['name'],
        password=hashed_password,
        default_currency_id=data.get('default_currency_id')
    )
    
    db.session.add(user)
    db.session.commit()
    
    # Create access token
    access_token = create_access_token(identity=user.id)
    
    return jsonify({
        'message': 'User created successfully',
        'access_token': access_token,
        'user': {
            'id': user.id,
            'name': user.name,
            'default_currency_id': user.default_currency_id
        }
    }), 201

@bp.route('/login', methods=['POST'])
def login():
    try:
        data = login_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    # Find user
    user = User.query.filter_by(name=data['name']).first()
    
    # Verify password
    if user and pbkdf2_sha256.verify(data['password'], user.password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user': {
                'id': user.id,
                'name': user.name,
                'default_currency_id': user.default_currency_id
            }
        }), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401
