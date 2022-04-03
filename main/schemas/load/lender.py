from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadLenderSchema(BaseSchema):
    lender_name = fields.String(validate=validate.Length(max=50), required=True)
    lent_money = fields.Float(validate=validate.Range(min=0), required=True)
