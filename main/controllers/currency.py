from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import BadRequest, Forbidden, NotFound
from main.engines import currency as currency_engine
from main.schemas.dump.currency import DumpCurrencySchema
from main.schemas.load.currency import LoadCurrencySchema
from main.models.currency import CurrencyModel
from main.schemas.base import PaginationSchema


def get_currency_data(currency: CurrencyModel):
    return {
        "id": currency.id,
        "name": currency.name,
        "abbreviation": currency.abbreviation,
        "created": currency.created,
        "updated": currency.updated,
    }


@app.post("/currencies")
@authenticate_user()
@pass_data(LoadCurrencySchema)
def create_currency(data, user):
    if not user.is_admin:
        raise Forbidden(
            error_message="You don't have permission to create new currency")

    if currency_engine.find_currency_by_name(data["name"]):
        raise BadRequest(error_message="Currency name has already been used")

    if currency_engine.find_currency_by_abbreviation(data["abbreviation"]):
        raise BadRequest(error_message="Currency abbreviation has already been used")

    currency = currency_engine.create_currency(data)

    return DumpCurrencySchema().jsonify(currency)


@app.get("/currencies")
@authenticate_user()
@pass_data(PaginationSchema)
def get_currencies(data, user_id):
    currencies, total_items = currency_engine.get_currencies(data)

    return jsonify(
        {
            "currencies": [
                get_currency_data(currency) for currency in currencies
            ],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
            "total_items": total_items,
        }
    )


@app.get("/currencies/<int:id>")
@authenticate_user()
def get_currency_by_id(user_id, id):
    currency = currency_engine.find_currency_by_id(id)

    if not currency:
        raise NotFound(error_message="Currency not found")

    return DumpCurrencySchema().jsonify(currency)


@app.put("/currencies/<int:id>")
@authenticate_user()
@pass_data(LoadCurrencySchema)
def update_currency_by_id(data, user, id):
    currency = currency_engine.find_currency_by_id(id)

    if not currency:
        raise NotFound(error_message="currency not found")

    if not user.is_admin:
        raise Forbidden(
            error_message="You don't have permission to update existing currency")

    currency_by_name = currency_engine.find_currency_by_name(data["name"])

    if currency_by_name and currency_by_name.id != currency.id:
        raise BadRequest(error_message="Currency name has already been used")

    currency_by_abbreviation = currency_engine.find_currency_by_abbreviation(
        data["abbreviation"])

    if currency_by_abbreviation and currency_by_abbreviation.id != currency.id:
        raise BadRequest(error_message="Currency abbreviation has already been used")

    updated_currency = currency_engine.update_currency(data, currency)

    return DumpCurrencySchema().jsonify(updated_currency)


@app.delete("/currencies/<int:id>")
@authenticate_user()
def delete_currency_by_id(user, id):
    currency = currency_engine.find_currency_by_id(id)

    if not currency:
        raise NotFound(error_message="Currency not found")

    if not user.is_admin:
        raise Forbidden(
            error_message="You don't have permission to delete existing currency")

    currency_engine.delete_currency(currency)

    return jsonify({})
