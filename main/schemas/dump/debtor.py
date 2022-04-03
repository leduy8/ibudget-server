from marshmallow import fields

from main.schemas.base import BaseSchema


class DumpDebtorSchema(BaseSchema):
    id = fields.Integer()
    debtor_name = fields.String()
    debt_money = fields.Float()
    user_id = fields.Integer()
    created = fields.DateTime()
    updated = fields.DateTime()
