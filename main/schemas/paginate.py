from marshmallow import fields

from main.schemas.base import PaginationSchema


class TransactionPaginationSchema(PaginationSchema):
    from_date = fields.Date(load_default=None)
    to_date = fields.Date(load_default=None)
