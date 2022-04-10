from main import db
from main.models.base import BaseModel


class DebtorModel(BaseModel):
    __tablename__ = "debtor"

    debtor_name = db.Column(db.String(50), nullable=False)
    debt_money = db.Column(db.Float(precision=2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __str__(self) -> str:
        return f"<DebtorModel {self.id} {self.user_id}>"
