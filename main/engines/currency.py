from typing import Dict, List

from main import db
from main.models.currency import CurrencyModel


def find_currency_by_name(name: str) -> CurrencyModel:
    return CurrencyModel.query.filter_by(name=name).first()


def find_currency_by_abbreviation(abbreviation: str) -> CurrencyModel:
    return CurrencyModel.query.filter_by(abbreviation=abbreviation).first()


def find_currency_by_id(id: int) -> CurrencyModel:
    return CurrencyModel.query.get(id)


def get_currency_count() -> int:
    return CurrencyModel.query.count()


def get_currencies(params: Dict) -> List[object]:
    """Returns list of list of currency model and count of total items"""
    currencies = CurrencyModel.query.paginate(
        params["page"], params["items_per_page"], False
    )

    return [currencies.items, currencies.total]


def create_currency(data: Dict, user_id: int) -> CurrencyModel:
    currency = CurrencyModel(
        name=data["name"], abbriviation=data["abbriviation"], user_id=user_id)

    db.session.add(currency)
    db.session.commit()

    return currency


def update_currency(data: Dict, currency: CurrencyModel) -> CurrencyModel:
    currency.name = data["name"]
    currency.abbreviation = data["abbriviation"]

    db.session.commit()

    return currency


def delete_currency(currency: CurrencyModel):
    db.session.delete(currency)
    db.session.commit()
