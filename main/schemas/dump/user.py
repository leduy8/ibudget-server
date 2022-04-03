from marshmallow import fields

from main.schemas.base import BaseSchema


class DumpUserSchema(BaseSchema):
    id = fields.Integer()
    username = fields.String()
    name = fields.String()
    password_salt = fields.String()
    created = fields.DateTime()
    updated = fields.DateTime()
