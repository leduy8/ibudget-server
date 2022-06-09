from main import db
from main.models.base import BaseModel


class BudgetModel(BaseModel):
    __tablename__ = "budget"

    title = db.Column(db.String(50), nullable=False)
    goal_value = db.Column(db.Float, nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    wallet_id = db.Column(db.Integer, db.ForeignKey("wallet.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    def __str__(self) -> str:
        return f"<BudgetModel {self.id}>"
