from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models import Category
from app.schemas import CategorySchema
from marshmallow import ValidationError

bp = Blueprint('category', __name__)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

@bp.route('/category', methods=['GET'])
@jwt_required()
def get_categories():
    categories = Category.query.all()
    return jsonify(categories_schema.dump(categories)), 200

@bp.route('/category/<int:category_id>', methods=['GET'])
@jwt_required()
def get_category(category_id):
    category = Category.query.get_or_404(category_id, description='Category not found')
    return jsonify(category_schema.dump(category)), 200

@bp.route('/category', methods=['POST'])
@jwt_required()
def create_category():
    try:
        data = category_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    category = Category(**data)
    db.session.add(category)
    db.session.commit()
    
    return jsonify(category_schema.dump(category)), 201

@bp.route('/category/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    category = Category.query.get_or_404(category_id, description='Category not found')
    db.session.delete(category)
    db.session.commit()
    
    return jsonify({'message': 'Category deleted'}), 200
