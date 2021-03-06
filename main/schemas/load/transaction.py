from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadTransactionSchema(BaseSchema):
    price = fields.Float(required=True)
    is_positive = fields.Boolean(required=True)
    note = fields.String(validate=validate.Length(max=200))
    created_date = fields.Date(required=True)
    category_id = fields.Integer(validate=validate.Range(min=1), required=True)
    wallet_id = fields.Integer(validate=validate.Range(min=1), required=True)
