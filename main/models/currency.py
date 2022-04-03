from main import db
from main.models.base import BaseModel


class CurrencyModel(BaseModel):
    __tablename__ = "currency"

    name = db.Column(db.String(40), unique=True, nullable=False)
    abbreviation = db.Column(db.String(3), unique=True, nullable=False)
    transactions = db.relationship(
        "TransactionModel", backref="currency", cascade="all, delete", lazy="dynamic"
    )

    def __str__(self) -> str:
        return f"<CurrencyModel {self.id} {self.name}>"
