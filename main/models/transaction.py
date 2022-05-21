from main import db
from main.models.base import BaseModel


class TransactionModel(BaseModel):
    __tablename__ = "transaction"

    price = db.Column(db.Float(precision=2), nullable=False)
    note = db.Column(db.String(200))
    is_positive = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    wallet_id = db.Column(db.Integer, db.ForeignKey("wallet.id"))

    def __str__(self) -> str:
        return f"<Transaction {self.id} {self.price} {self.user_id}>"
