from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import Forbidden, NotFound, BadRequest
from main.engines import debtor as debtor_engine
from main.schemas.base import PaginationSchema, TransactSchema
from main.models.debtor import DebtorModel
from main.schemas.dump.debtor import DumpDebtorSchema
from main.schemas.load.debtor import LoadDebtorSchema


def get_debtor_data(debtor: DebtorModel):
    return {
        "id": debtor.id,
        "debtor_name": debtor.debtor_name,
        "debt_money": debtor.debt_money,
        "user_id": debtor.user_id,
        "created": debtor.created,
        "updated": debtor.updated,
    }


@app.post("/debtors")
@authenticate_user()
@pass_data(LoadDebtorSchema)
def create_debtor(data, user):
    debtor = debtor_engine.create_debtor(data, user.id)

    return DumpDebtorSchema().jsonify(debtor)


@app.get("/debtors")
@authenticate_user()
@pass_data(PaginationSchema)
def get_debtors(data, user):
    debtors, total_items = debtor_engine.get_debtors(data)

    return jsonify(
        {
            "debtors": [
                get_debtor_data(debtor) for debtor in debtors
            ],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
            "total_items": total_items,
        }
    )


@app.get("/debtors/<int:id>")
@authenticate_user()
def get_debtor_by_id(user, id):
    debtor = debtor_engine.find_debtor_by_id(id)

    if not debtor:
        raise NotFound(error_message="Debtor not found")

    return DumpDebtorSchema().jsonify(debtor)


@app.put("/debtors/<int:id>")
@authenticate_user()
@pass_data(LoadDebtorSchema)
def update_debtor_by_id(data, user, id):
    debtor = debtor_engine.find_debtor_by_id(id)

    if not debtor:
        raise NotFound(error_message="Debtor not found")

    if debtor.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this debtor"
        )

    updated_debtor = debtor_engine.update_debtor(data, debtor)

    return DumpDebtorSchema().jsonify(updated_debtor)


@app.delete("/debtors/<int:id>")
@authenticate_user()
def delete_debtor_by_id(user, id):
    debtor = debtor_engine.find_debtor_by_id(id)

    if not debtor:
        raise NotFound(error_message="Debtor not found")

    if debtor.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to delete this debtor"
        )

    debtor_engine.delete_debtor(debtor)

    return jsonify({})


@app.put("/debtors/<int:id>/transaction")
@authenticate_user()
@pass_data(TransactSchema)
def transact_in_debtor(data, user, id):
    debtor = debtor_engine.find_debtor_by_id(id)

    if not debtor:
        raise NotFound(error_message="Debtor not found")

    if debtor.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this debtor"
        )

    if debtor.debt_money - data["price"] < 0:
        raise BadRequest(error_message="Balance is not suffice this transaction")

    updated_debtor = debtor_engine.transact_in_debtor(data, debtor)

    return DumpDebtorSchema().jsonify(updated_debtor)
