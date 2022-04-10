from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadWalletSchema(BaseSchema):
    name = fields.String(validate=validate.Length(max=50), required=True)
    balance = fields.Float(validate=validate.Range(min=0), required=True)


class LoadUpdateWalletSchema(BaseSchema):
    name = fields.String(validate=validate.Length(max=50), required=True)


class LoadTransactionWalletSchema(BaseSchema):
    price = fields.Float(required=True)
