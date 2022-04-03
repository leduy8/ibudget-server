from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadTransactionSchema(BaseSchema):
    price = fields.String(validate=validate.Length(max=50), required=True)
    is_positive = fields.Boolean(required=True)
    note = fields.String(validate=validate.Length(max=200), required=True)
    category_id = fields.Integer(validate=validate.Range(min=1), required=True)
    currency_id = fields.Integer(validate=validate.Range(min=1), required=True)
