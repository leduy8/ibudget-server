from typing import Dict, List

from main import db
from main.models.debtor import DebtorModel


def find_debtor_by_name(name: str) -> DebtorModel:
    return DebtorModel.query.filter_by(debtor_name=name).first()


def find_debtor_by_id(id: int) -> DebtorModel:
    return DebtorModel.query.get(id)


def get_debtor_count() -> int:
    return DebtorModel.query.count()


def get_debtors(params: Dict) -> List[object]:
    """Returns list of list of debtor model and count of total items"""
    debtors = DebtorModel.query.paginate(
        params["page"], params["items_per_page"], False
    )

    return [debtors.items, debtors.total]


def create_debtor(data: Dict, user_id: int) -> DebtorModel:
    debtor = DebtorModel(
        debtor_name=data["debtor_name"],
        user_id=user_id,
        debt_money=data["debt_money"]
    )

    db.session.add(debtor)
    db.session.commit()

    return debtor


def update_debtor(data: Dict, debtor: DebtorModel) -> DebtorModel:
    debtor.debtor_name = data["debtor_name"]

    db.session.commit()

    return debtor


def delete_debtor(debtor: DebtorModel):
    db.session.delete(debtor)
    db.session.commit()


def transaction_in_debtor(data: Dict, debtor: DebtorModel):
    debtor.debt_money += data["price"]

    db.session.commit()

    return debtor
