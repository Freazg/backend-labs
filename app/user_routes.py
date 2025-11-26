from flask import Blueprint, jsonify, request
from app import db
from app.models import User
from app.schemas import UserSchema
from marshmallow import ValidationError

bp = Blueprint('user', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id, description='User not found')
    return jsonify(user_schema.dump(user)), 200

@bp.route('/user', methods=['POST'])
def create_user():
    try:
        data = user_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    
    return jsonify(user_schema.dump(user)), 201

@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id, description='User not found')
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted'}), 200
