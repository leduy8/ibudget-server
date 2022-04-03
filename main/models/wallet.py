from main import db
from main.models.base import BaseModel


class WalletModel(BaseModel):
    __tablename__ = "wallet"

    name = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    transactions = db.relationship(
        "TransactionModel", backref="wallet", cascade="all,delete", lazy="dynamic"
    )

    def __str__(self) -> str:
        return f"<WalletModel {self.id} {self.name}>"
