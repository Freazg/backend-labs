from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models import Record, User, Category
from app.schemas import RecordSchema
from marshmallow import ValidationError

bp = Blueprint('record', __name__)
record_schema = RecordSchema()
records_schema = RecordSchema(many=True)

@bp.route('/record', methods=['GET'])
@jwt_required()
def get_records():
    user_id = request.args.get('user_id', type=int)
    category_id = request.args.get('category_id', type=int)
    
    if user_id is None and category_id is None:
        return jsonify({'error': 'user_id or category_id parameter is required'}), 400
    
    query = Record.query
    
    if user_id is not None:
        query = query.filter_by(user_id=user_id)
    if category_id is not None:
        query = query.filter_by(category_id=category_id)
    
    records = query.all()
    return jsonify(records_schema.dump(records)), 200

@bp.route('/record/<int:record_id>', methods=['GET'])
@jwt_required()
def get_record(record_id):
    record = Record.query.get_or_404(record_id, description='Record not found')
    return jsonify(record_schema.dump(record)), 200

@bp.route('/record', methods=['POST'])
@jwt_required()
def create_record():
    try:
        data = record_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    category = Category.query.get(data['category_id'])
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    
    if 'currency_id' not in data or data['currency_id'] is None:
        data['currency_id'] = user.default_currency_id
    
    record = Record(**data)
    db.session.add(record)
    db.session.commit()
    
    return jsonify(record_schema.dump(record)), 201

@bp.route('/record/<int:record_id>', methods=['DELETE'])
@jwt_required()
def delete_record(record_id):
    record = Record.query.get_or_404(record_id, description='Record not found')
    db.session.delete(record)
    db.session.commit()
    
    return jsonify({'message': 'Record deleted'}), 200
