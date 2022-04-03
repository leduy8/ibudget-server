from marshmallow import fields

from main.schemas.base import BaseSchema


class DumpLenderSchema(BaseSchema):
    id = fields.Integer()
    lender_name = fields.String()
    lent_money = fields.Float()
    user_id = fields.Integer()
    created = fields.DateTime()
    updated = fields.DateTime()
