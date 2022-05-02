from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import BadRequest, Forbidden, NotFound
from main.engines import wallet as wallet_engine
from main.models.wallet import WalletModel
from main.schemas.base import PaginationSchema, TransactSchema
from main.schemas.dump.wallet import DumpWalletSchema
from main.schemas.load.wallet import LoadUpdateWalletSchema, LoadWalletSchema


def get_wallet_data(wallet: WalletModel):
    return {
        "id": wallet.id,
        "name": wallet.name,
        "user_id": wallet.user_id,
        "created": wallet.created,
        "updated": wallet.updated,
    }


@app.post("/wallets")
@authenticate_user()
@pass_data(LoadWalletSchema)
def create_wallet(data, user):
    if wallet_engine.check_existing_wallet_of_user(user.id, data["name"]):
        raise BadRequest(error_message="Wallet name has already been used ")

    wallet = wallet_engine.create_wallet(data, user.id)

    return DumpWalletSchema().jsonify(wallet)


@app.get("/wallets")
@authenticate_user()
@pass_data(PaginationSchema)
def get_wallets(data, user):
    wallets, total_items = wallet_engine.get_wallets(data)

    return jsonify(
        {
            "wallets": [get_wallet_data(wallet) for wallet in wallets],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
            "total_items": total_items,
        }
    )


@app.get("/wallets/<int:id>")
@authenticate_user()
def get_wallet_by_id(user, id):
    wallet = wallet_engine.find_wallet_by_id(id)

    if not wallet:
        raise NotFound(error_message="Wallet not found")

    return DumpWalletSchema().jsonify(wallet)


@app.put("/wallets/<int:id>")
@authenticate_user()
@pass_data(LoadUpdateWalletSchema)
def update_wallet_by_id(data, user, id):
    wallet = wallet_engine.find_wallet_by_id(id)

    if not wallet:
        raise NotFound(error_message="Wallet not found")

    if wallet.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this wallet"
        )

    updated_wallet = wallet_engine.update_wallet(data, wallet)

    return DumpWalletSchema().jsonify(updated_wallet)


@app.delete("/wallets/<int:id>")
@authenticate_user()
def delete_wallet_by_id(user, id):
    wallet = wallet_engine.find_wallet_by_id(id)

    if not wallet:
        raise NotFound(error_message="Wallet not found")

    if wallet.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to delete this wallet"
        )

    wallet_engine.delete_wallet(wallet)

    return jsonify({})


@app.put("/wallets/<int:id>/transaction")
@authenticate_user()
@pass_data(TransactSchema)
def transact_in_wallet(data, user, id):
    wallet = wallet_engine.find_wallet_by_id(id)

    if not wallet:
        raise NotFound(error_message="Wallet not found")

    if wallet.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this wallet"
        )

    if wallet.balance + data["price"] < 0:
        raise BadRequest(error_message="Balance is not suffice this transaction")

    updated_wallet = wallet_engine.transact_in_wallet(data, wallet)

    return DumpWalletSchema().jsonify(updated_wallet)
