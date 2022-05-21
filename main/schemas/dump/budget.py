from marshmallow import fields

from main.schemas.base import BaseSchema


class DumpBudgetSchema(BaseSchema):
    id = fields.Integer()
    goal_value = fields.Float()
    from_date = fields.Date()
    to_date = fields.Date()
    created = fields.DateTime()
    updated = fields.DateTime()
    user_id = fields.Integer()
    wallet_id = fields.Integer()
    category_id = fields.Integer()
