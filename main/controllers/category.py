import json

from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import NotFound
from main.engines import category as category_engine
from main.schemas.base import PaginationSchema
from main.schemas.dump.category import DumpCategorySchema


@app.get("/categories")
@authenticate_user()
@pass_data(PaginationSchema)
def get_categories(data, user):
    categories, total_items = category_engine.get_categories()

    return jsonify(
        {
            "categories": json.loads(DumpCategorySchema().dumps(categories, many=True)),
            "total_items": total_items,
        }
    )


@app.get("/categories/<int:id>")
@authenticate_user()
def get_category_by_id(user, id):
    category = category_engine.find_category_by_id(id)

    if not category:
        raise NotFound(error_message="Category not found")

    return DumpCategorySchema().jsonify(category)
