from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadCurrencySchema(BaseSchema):
    name = fields.String(validate=validate.Length(max=50), required=True)
    abbreviation = fields.String(validate=validate.Length(equal=3), required=True)
