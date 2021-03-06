from marshmallow import fields

from main.schemas.base import BaseSchema


class DumpTransactionSchema(BaseSchema):
    id = fields.Integer()
    price = fields.Float()
    is_positive = fields.Boolean()
    note = fields.String()
    created_date = fields.Date()
    created = fields.DateTime()
    updated = fields.DateTime()
    user_id = fields.Integer()
    category_id = fields.Integer()
    wallet_id = fields.Integer()
