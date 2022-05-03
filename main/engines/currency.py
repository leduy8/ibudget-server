from typing import Dict, List

from main import db
from main.models.currency import CurrencyModel


def find_currency_by_id(id: int) -> CurrencyModel:
    return CurrencyModel.query.get(id)


def create_currency(data: Dict):
    currency = CurrencyModel(name=data["name"], abbreviation=data["abbreviation"])

    db.session.add(currency)
    db.session.commit()

    return currency


def get_currencies() -> List[object]:
    currencies = CurrencyModel.query.all()

    return [currencies, len(currencies)]
