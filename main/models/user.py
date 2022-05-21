from main import db
from main.models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    password_salt = db.Column(db.String(12), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    wallets = db.relationship(
        "WalletModel", backref="owner", cascade="all,delete", lazy="dynamic"
    )
    transactions = db.relationship(
        "TransactionModel", backref="owner", cascade="all,delete", lazy="dynamic"
    )
    lenders = db.relationship(
        "LenderModel", backref="debtor", cascade="all,delete", lazy="dynamic"
    )
    debtors = db.relationship(
        "DebtorModel", backref="lender", cascade="all,delete", lazy="dynamic"
    )
    budgets = db.relationship(
        "BudgetModel", backref="owner", cascade="all,delete", lazy="dynamic"
    )

    def __str__(self) -> str:
        return f"<UserModel {self.id} {self.username}>"
