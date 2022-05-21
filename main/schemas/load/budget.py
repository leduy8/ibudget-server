from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class LoadBudgetSchema(BaseSchema):
    goal_value = fields.Float(required=True)
    from_date = fields.Date(required=True)
    to_date = fields.Date(required=True)
    category_id = fields.Integer(validate=validate.Range(min=1), required=True)
    wallet_id = fields.Integer(validate=validate.Range(min=1), required=True)
