from marshmallow import fields

from main.schemas.base import BaseSchema


class DumpCurrencySchema(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    abbriviation = fields.String()
    created = fields.DateTime()
    updated = fields.DateTime()
