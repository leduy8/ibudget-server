import json

from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user
from main.commons.exceptions import NotFound
from main.engines import currency as currency_engine
from main.schemas.dump.currency import DumpCurrencySchema


@app.get("/currencies")
@authenticate_user()
def get_currencies(user):
    currencies, total_items = currency_engine.get_currencies()

    return jsonify(
        {
            "currencies": json.loads(DumpCurrencySchema().dumps(currencies, many=True)),
            "total_items": total_items,
        }
    )


@app.get("/currencies/<int:id>")
@authenticate_user()
def get_currency_by_id(user, id):
    currency = currency_engine.find_currency_by_id(id)

    if not currency:
        raise NotFound(error_message="Currency not found")

    return DumpCurrencySchema().jsonify(currency)
