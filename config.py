import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password123@localhost:5432/expense_tracker')
SQLALCHEMY_TRACK_MODIFICATIONS = False
API_TITLE = 'Expense Tracker API'
API_VERSION = 'v1'
OPENAPI_VERSION = '3.0.2'
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev-jwt-secret-key-for-testing-12345')
