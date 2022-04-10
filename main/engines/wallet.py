from typing import Dict, List

from main import db
from main.models.wallet import WalletModel


def find_wallet_by_name(name: str) -> WalletModel:
    return WalletModel.query.filter_by(name=name).first()


def find_wallet_by_id(id: int) -> WalletModel:
    return WalletModel.query.get(id)


def get_wallet_count() -> int:
    return WalletModel.query.count()


def check_existing_wallet_of_user(user_id: int, name: str) -> WalletModel:
    return WalletModel.query.filter_by(user_id=user_id).filter_by(name=name).first()


def get_wallets(params: Dict) -> List[object]:
    """Returns list of list of wallet model and count of total items"""
    wallets = WalletModel.query.paginate(
        params["page"], params["items_per_page"], False
    )

    return [wallets.items, wallets.total]


def create_wallet(data: Dict, user_id: int) -> WalletModel:
    wallet = WalletModel(
        name=data["name"],
        user_id=user_id,
        balance=data["balance"]
    )

    db.session.add(wallet)
    db.session.commit()

    return wallet


def update_wallet(data: Dict, wallet: WalletModel) -> WalletModel:
    wallet.name = data["name"]

    db.session.commit()

    return wallet


def delete_wallet(wallet: WalletModel):
    db.session.delete(wallet)
    db.session.commit()


def transact_in_wallet(data: Dict, wallet: WalletModel):
    wallet.balance += data["price"]

    db.session.commit()

    return wallet
