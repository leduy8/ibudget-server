from flask import Response, redirect
from flask_admin.contrib import sqla
from werkzeug.exceptions import HTTPException

from main import admin, basic_auth, db
from main.models.budget import BudgetModel
from main.models.category import CategoryModel
from main.models.debtor import DebtorModel
from main.models.lender import LenderModel
from main.models.transaction import TransactionModel
from main.models.user import UserModel
from main.models.wallet import WalletModel


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                message, 401, {"WWW-Authenticate": 'Basic realm="Login Required"'}
            ),
        )


class ModelView(sqla.ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException("Not authenticated. Refresh the page.")
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


user_model_view = ModelView(
    UserModel,
    db.session,
    name="User",
)

category_model_view = ModelView(
    CategoryModel,
    db.session,
    name="Category",
)

wallet_model_view = ModelView(
    WalletModel,
    db.session,
    name="Wallet",
)

transaction_model_view = ModelView(
    TransactionModel,
    db.session,
    name="Transaction",
)
debtor_model_view = ModelView(
    DebtorModel,
    db.session,
    name="Debtor",
)
lender_model_view = ModelView(
    LenderModel,
    db.session,
    name="Lender",
)
budget_model_view = ModelView(
    BudgetModel,
    db.session,
    name="Budget",
)

admin.add_view(user_model_view)
admin.add_view(category_model_view)
admin.add_view(wallet_model_view)
admin.add_view(transaction_model_view)
# admin.add_view(debtor_model_view)
# admin.add_view(lender_model_view)
admin.add_view(budget_model_view)
