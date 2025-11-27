from marshmallow import Schema, fields, validate

class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    code = fields.Str(required=True, validate=validate.Length(min=3, max=3))
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    default_currency_id = fields.Int(required=False, allow_none=True)

class UserLoginSchema(Schema):
    name = fields.Str(required=True)
    password = fields.Str(required=True)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    currency_id = fields.Int(required=False, allow_none=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
