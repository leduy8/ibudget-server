from main import db
from main.models.base import BaseModel


class LenderModel(BaseModel):
    __tablename__ = "Lender"

    lender_name = db.Column(db.String(50), nullable=False)
    lent_money = db.Column(db.Float(precision=2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __str__(self) -> str:
        return f"<LenderModel {self.id} {self.user_id}>"
