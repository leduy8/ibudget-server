from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadDebtorSchema(BaseSchema):
    debtor_name = fields.String(validate=validate.Length(max=50), required=True)
    debt_money = fields.Float(validate=validate.Range(min=0), required=True)
