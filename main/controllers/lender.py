from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import Forbidden, NotFound
from main.engines import lender as lender_engine
from main.schemas.dump.lender import DumpLenderSchema
from main.schemas.load.lender import LoadLenderSchema
from main.schemas.base import PaginationSchema


@app.post("/lenders")
@authenticate_user()
@pass_data(LoadLenderSchema)
def create_lender(data, user):
    lender = lender_engine.create_lender(data, user.id)

    return DumpLenderSchema().jsonify(lender)


@app.get("/lenders")
@authenticate_user(required=False)
@pass_data(PaginationSchema)
def get_lenders(data, user):
    lenders, total_items = lender_engine.get_lenders(data)

    return jsonify(
        {
            "lenders": [
                lender for lender in lenders
            ],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
            "total_items": total_items,
        }
    )


@app.get("/lenders/<int:id>")
@authenticate_user(required=False)
def get_lender_by_id(user, id):
    lender = lender_engine.find_lender_by_id(id)

    if not lender:
        raise NotFound(error_message="Lender not found")

    return DumpLenderSchema().jsonify(lender)


@app.put("/lenders/<int:id>")
@authenticate_user()
@pass_data(LoadLenderSchema)
def update_lender_by_id(data, user, id):
    lender = lender_engine.find_lender_by_id(id)

    if not lender:
        raise NotFound(error_message="Lender not found")

    if lender.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this lender"
        )

    updated_lender = lender_engine.update_lender(data, lender)

    return DumpLenderSchema().jsonify(updated_lender)


@app.delete("/lenders/<int:id>")
@authenticate_user()
def delete_lender_by_id(user_id, id):
    lender = lender_engine.find_lender_by_id(id)

    if not lender:
        raise NotFound(error_message="Lender not found")

    if lender.user_id != user_id:
        raise Forbidden(
            error_message="User doesn't have permission to delete this lender"
        )

    lender_engine.delete_lender(lender)

    return jsonify({})
