from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadAuthSchema(BaseSchema):
    username = fields.String(validate=validate.Length(max=50), required=True)
    password = fields.String(validate=validate.Length(min=6, max=32), required=True)
