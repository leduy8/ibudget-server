from marshmallow import fields

from main.schemas.base import BaseSchema


class DumpWalletSchema(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    balance = fields.Float()
    user_id = fields.Integer()
    created = fields.DateTime()
    updated = fields.DateTime()
