from typing import Dict, List

from main import db
from main.models.lender import LenderModel


def find_lender_by_name(name: str) -> LenderModel:
    return LenderModel.query.filter_by(lender_name=name).first()


def find_lender_by_id(id: int) -> LenderModel:
    return LenderModel.query.get(id)


def get_lender_count() -> int:
    return LenderModel.query.count()


def get_lenders(params: Dict) -> List[object]:
    """Returns list of list of lender model and count of total items"""
    lenders = LenderModel.query.paginate(
        params["page"], params["items_per_page"], False
    )

    return [lenders.items, lenders.total]


def create_lender(data: Dict, user_id: int) -> LenderModel:
    lender = LenderModel(
        lender_name=data["lender_name"],
        user_id=user_id,
        lent_money=data["lent_money"]
    )

    db.session.add(lender)
    db.session.commit()

    return lender


def update_lender(data: Dict, lender: LenderModel) -> LenderModel:
    lender.lender_name = data["lender_name"]
    lender.lent_money = data["lent_money"]

    db.session.commit()

    return lender


def delete_lender(lender: LenderModel):
    db.session.delete(lender)
    db.session.commit()


def transact_in_lender(data: Dict, lender: LenderModel):
    lender.lent_money -= data["price"]

    db.session.commit()

    return lender
