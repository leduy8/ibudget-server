from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import BadRequest, Forbidden, NotFound
from main.engines import category as category_engine
from main.models.category import CategoryModel
from main.schemas.dump.category import DumpCategorySchema
from main.schemas.load.category import LoadCategorySchema
from main.schemas.paginate import CategoryPaginationSchema


def get_category_data(category: CategoryModel):
    return {
        "name": category.name,
        "user_id": category.user_id,
        "created": category.created,
        "updated": category.updated,
    }


@app.post("/categories")
@authenticate_user()
@pass_data(LoadCategorySchema)
def create_category(data, user):
    if category_engine.check_existing_category_of_user(user.id, data["name"]):
        raise BadRequest(error_message="Category name has already been used")

    category = category_engine.create_category(data, user.id)

    return DumpCategorySchema().jsonify(category)


@app.get("/categories")
@authenticate_user()
@pass_data(CategoryPaginationSchema)
def get_categories(data, user):
    categories, total_items = category_engine.get_categories(data)

    return jsonify(
        {
            "categories": [get_category_data(category) for category in categories],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
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


@app.put("/categories/<int:id>")
@authenticate_user()
@pass_data(LoadCategorySchema)
def update_category_by_id(data, user, id):
    category = category_engine.find_category_by_id(id)

    if not category:
        raise NotFound(error_message="Category not found")

    if category.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this category"
        )

    category_by_name = category_engine.check_existing_category_of_user(
        user.id, data["name"]
    )

    if category_by_name and category_by_name.id != category.id:
        raise BadRequest(error_message="Category name has already been used")

    updated_category = category_engine.update_category(data, category)

    return DumpCategorySchema().jsonify(updated_category)


@app.delete("/categories/<int:id>")
@authenticate_user()
def delete_category_by_id(user, id):
    category = category_engine.find_category_by_id(id)

    if not category:
        raise NotFound(error_message="Category not found")

    if category.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to delete this category"
        )

    category_engine.delete_category(category)

    return jsonify({})
