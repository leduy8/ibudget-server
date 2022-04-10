from typing import Dict, List

from main import db
from main.models.transaction import TransactionModel


def find_transaction_by_id(id: int) -> TransactionModel:
    return TransactionModel.query.get(id)


def get_transaction_count() -> int:
    return TransactionModel.query.count()


def get_transactions(params: Dict) -> List[object]:
    """Returns list of list of transaction model and count of total items"""
    transactions = TransactionModel.query.paginate(
        params["page"], params["items_per_page"], False
    )

    return [transactions.items, transactions.total]


def create_transaction(data: Dict, user_id: int) -> TransactionModel:
    transaction = TransactionModel(
        price=data["price"],
        is_positive=data["is_positive"],
        user_id=user_id,
        currency_id=data["currency_id"],
        wallet_id=data["wallet_id"],
        category_id=data["category_id"]
    )

    if "note" in data:
        transaction.note = data["note"]

    db.session.add(transaction)
    db.session.commit()

    return transaction


def update_transaction(data: Dict, transaction: TransactionModel) -> TransactionModel:
    transaction.price = data["price"]
    transaction.is_positive = data["is_positive"]
    transaction.currency_id = data["currency_id"]
    transaction.wallet_id = data["wallet_id"]
    transaction.category_id = data["category_id"]

    if "note" in data:
        transaction.note = data["note"]

    db.session.commit()

    return transaction


def delete_transaction(transaction: TransactionModel):
    db.session.delete(transaction)
    db.session.commit()
