from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import BadRequest, Forbidden, NotFound
from main.engines import wallet as wallet_engine
from main.schemas.base import PaginationSchema
from main.schemas.dump.wallet import DumpWalletSchema
from main.schemas.load.wallet import (
    LoadTransactionWalletSchema,
    LoadUpdateWalletSchema,
    LoadWalletSchema,
)


@app.post("/wallets")
@authenticate_user()
@pass_data(LoadWalletSchema)
def create_wallet(data, user):
    wallet = wallet_engine.create_wallet(data, user.id)

    return DumpWalletSchema().jsonify(wallet)


@app.get("/wallets")
@authenticate_user(required=False)
@pass_data(PaginationSchema)
def get_wallets(data, user):
    wallets, total_items = wallet_engine.get_wallets(data)

    return jsonify(
        {
            "wallets": [
                wallet for wallet in wallets
            ],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
            "total_items": total_items,
        }
    )


@app.get("/wallets/<int:id>")
@authenticate_user(required=False)
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
def delete_wallet_by_id(user_id, id):
    wallet = wallet_engine.find_wallet_by_id(id)

    if not wallet:
        raise NotFound(error_message="Wallet not found")

    if wallet.user_id != user_id:
        raise Forbidden(
            error_message="User doesn't have permission to delete this wallet"
        )

    wallet_engine.delete_wallet(wallet)

    return jsonify({})


@app.put("/wallets/<int:id>/transaction")
@authenticate_user()
@pass_data(LoadTransactionWalletSchema)
def transact_in_wallet(data, user, id):
    wallet = wallet_engine.find_wallet_by_id(id)

    if not wallet:
        raise NotFound(error_message="Wallet not found")

    if wallet.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this wallet"
        )

    if wallet.balance < data["price"]:
        raise BadRequest(error_message="Balance is not suffice this transaction")

    updated_wallet = wallet_engine.transact_in_wallet(data, wallet)

    return DumpWalletSchema().jsonify(updated_wallet)
