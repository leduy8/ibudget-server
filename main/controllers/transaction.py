from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import Forbidden, NotFound
from main.engines import category as category_engine
from main.engines import transaction as transaction_engine
from main.engines import wallet as wallet_engine
from main.schemas.dump.transaction import DumpTransactionSchema
from main.schemas.load.transaction import LoadTransactionSchema
from main.schemas.paginate import TransactionPaginationSchema


@app.post("/transactions")
@authenticate_user()
@pass_data(LoadTransactionSchema)
def create_transaction(data, user):
    if not category_engine.find_category_by_id(data["category_id"]):
        raise NotFound(error_message="Category not found")

    if not wallet_engine.find_wallet_by_id(data["wallet_id"]):
        raise NotFound(error_message="Wallet not found")

    transaction = transaction_engine.create_transaction(data, user.id)

    return DumpTransactionSchema().jsonify(transaction)


@app.get("/transactions")
@authenticate_user()
@pass_data(TransactionPaginationSchema)
def get_transactions(data, user):
    transactions, total_items = transaction_engine.get_transactions(data, user.id)

    return jsonify(
        {
            "transactions": [
                DumpTransactionSchema().dump(transaction)
                for transaction in transactions
            ],
            "from": data["from_date"],
            "to": data["to_date"],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
            "total_items": total_items,
        }
    )


@app.get("/transactions/<int:id>")
@authenticate_user()
def get_transaction_by_id(user, id):
    transaction = transaction_engine.find_transaction_by_id(id)

    if not transaction:
        raise NotFound(error_message="Transaction not found")

    return DumpTransactionSchema().jsonify(transaction)


@app.put("/transactions/<int:id>")
@authenticate_user()
@pass_data(LoadTransactionSchema)
def update_transaction_by_id(data, user, id):
    transaction = transaction_engine.find_transaction_by_id(id)

    if not transaction:
        raise NotFound(error_message="Transaction not found")

    if transaction.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this transaction"
        )

    if not category_engine.find_category_by_id(data["category_id"]):
        raise NotFound(error_message="Category not found")

    if not wallet_engine.find_wallet_by_id(data["wallet_id"]):
        raise NotFound(error_message="Wallet not found")

    updated_transaction = transaction_engine.update_transaction(data, transaction)

    return DumpTransactionSchema().jsonify(updated_transaction)


@app.delete("/transactions/<int:id>")
@authenticate_user()
def delete_transaction_by_id(user, id):
    transaction = transaction_engine.find_transaction_by_id(id)

    if not transaction:
        raise NotFound(error_message="Transaction not found")

    if transaction.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to delete this transaction"
        )

    transaction_engine.delete_transaction(transaction)

    return jsonify({})
