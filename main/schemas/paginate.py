from marshmallow import fields, validate

from main import config
from main.schemas.base import PaginationSchema


class CategoryPaginationSchema(PaginationSchema):
    items_per_page = fields.Integer(
        load_default=config.CATEGORIES_PER_PAGE, validate=validate.Range(min=1)
    )
    

class TransactionPaginationSchema(PaginationSchema):
    from_date = fields.Date()
    to_date = fields.Date()
