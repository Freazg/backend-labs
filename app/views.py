from flask import Blueprint, jsonify
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Backend Labs API',
        'status': 'running',
        'endpoints': {
            'healthcheck': '/healthcheck'
        }
    }), 200

@bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({
        'status': 'OK',
        'date': datetime.now().isoformat()
    }), 200
