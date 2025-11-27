from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py', silent=True)
    
    # JWT Configuration - Fixed key for development
    app.config['JWT_SECRET_KEY'] = 'dev-jwt-secret-key-for-testing-12345'
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'message': 'The token has expired.',
            'error': 'token_expired'
        }), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'message': 'Signature verification failed.',
            'error': 'invalid_token'
        }), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            'description': 'Request does not contain an access token.',
            'error': 'authorization_required'
        }), 401
    
    with app.app_context():
        from app import models
        
        # Register blueprints
        from app.views import bp as main_bp
        from app.auth_routes import bp as auth_bp
        from app.currency_routes import bp as currency_bp
        from app.user_routes import bp as user_bp
        from app.category_routes import bp as category_bp
        from app.record_routes import bp as record_bp
        
        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(currency_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(category_bp)
        app.register_blueprint(record_bp)
        
    return app
