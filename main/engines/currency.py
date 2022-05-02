from main.models.currency import CurrencyModel


def find_currency_by_id(id: int) -> CurrencyModel:
    return CurrencyModel.query.get(id)
